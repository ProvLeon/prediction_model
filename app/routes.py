from flask import Blueprint, request, jsonify
from app import db
from app.models import Student, Location, Pattern
from app.ml_model import pattern_tracker
from app.shared_data import real_time_locations
from sqlalchemy.exc import IntegrityError
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/api/update_location', methods=['POST'])
def update_location():
    print("Received request:", request.json)

    data = request.json
    student_id = data['student_id']
    latitude = data['latitude']
    longitude = data['longitude']

    try:
        # Check if the student exists
        student = Student.query.get(student_id)
        if not student:
            # If student doesn't exist, create a new one
            student = Student(id=student_id, name=data.get('name', 'Unknown'),
                              email=data.get('email', f'{student_id}@example.com'),
                              phone=data.get('phone', '0000000000'))
            db.session.add(student)
            db.session.flush()  # This will assign the ID if it's auto-incrementing

        # Get the most recent location for this student
        latest_location = Location.query.filter_by(student_id=student_id).order_by(Location.timestamp.desc()).first()

        if latest_location:
            # Update the existing location
            latest_location.latitude = latitude
            latest_location.longitude = longitude
            latest_location.timestamp = datetime.utcnow()
        else:
            # Create a new location
            new_location = Location(student_id=student_id, latitude=latitude, longitude=longitude)
            db.session.add(new_location)

        db.session.commit()

        real_time_locations[student_id] = (latitude, longitude)

        return jsonify({'message': 'Location updated successfully'}), 200

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Integrity error. Possibly duplicate unique field.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/api/get_patterns/<string:student_id>', methods=['GET'])
def get_patterns(student_id):
    locations = Location.query.filter_by(student_id=student_id).all()

    try:
        patterns = pattern_tracker.train(locations)

        if len(patterns) > 0:
            pattern = Pattern(student_id=student_id, pattern_data=patterns)
            db.session.add(pattern)
            db.session.commit()
            print(f'pattern {pattern}')
            return jsonify({'message': 'Patterns generated successfully', 'pattern': patterns.tolist()}), 200
        else:
            return jsonify({'message': 'Not enough data to generate patterns'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@bp.route('/api/student_patterns/<string:student_id>', methods=['GET'])
def get_student_patterns(student_id):
    try:
        # Check if the student exists
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        # Get the latest pattern
        latest_pattern = Pattern.query.filter_by(student_id=student_id).order_by(Pattern.id.desc()).first()

        # Get recent locations (last 50 for example)
        recent_locations = Location.query.filter_by(student_id=student_id).order_by(Location.timestamp.desc()).limit(50).all()

        # Prepare the response data
        pattern_data = latest_pattern.pattern_data.tolist() if latest_pattern else None
        locations_data = [
            {
                'latitude': loc.latitude,
                'longitude': loc.longitude,
                'timestamp': loc.timestamp.isoformat()
            } for loc in recent_locations
        ]

        response_data = {
            'student_id': student_id,
            'latest_pattern': pattern_data,
            'recent_locations': locations_data
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
