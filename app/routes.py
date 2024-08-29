from flask import Blueprint, request, jsonify
from app import db
from app.models import Student, Location, Pattern
from app.ml_model import pattern_tracker
from app.shared_data import real_time_locations
from sqlalchemy.exc import IntegrityError

bp = Blueprint('main', __name__)

@bp.route('/api/update_location', methods=['POST'])
def update_location():
    data = request.json
    student_id = data['student_id']
    latitude = data['latitude']
    longitude = data['longitude']

    try:
        student = Student.query.get(student_id)
        if not student:
            # Only create a new student if it doesn't exist
            student = Student(
                id=student_id,
                name=data.get('name', f'Student {student_id}'),
                email=data.get('email', f'{student_id}@example.com'),
                phone=data.get('phone', f'000-{student_id}')
            )
            db.session.add(student)

        new_location = Location(student_id=student_id, latitude=latitude, longitude=longitude)
        db.session.add(new_location)
        db.session.commit()

        real_time_locations[student_id] = (latitude, longitude)

        return jsonify({'message': 'Location updated successfully'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error. Student already exists.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/api/get_patterns/<string:student_id>', methods=['GET'])
def get_patterns(student_id):
    locations = Location.query.filter_by(student_id=student_id).all()

    try:
        patterns = pattern_tracker.train(locations)
        new_pattern = Pattern(student_id=student_id, pattern_data=patterns)
        db.session.add(new_pattern)
        db.session.commit()

        return jsonify({'message': 'Patterns generated successfully', 'pattern': patterns.tolist()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@bp.route('/api/student_patterns/<string:student_id>', methods=['GET'])
def get_student_patterns(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        latest_pattern = Pattern.query.filter_by(student_id=student_id).order_by(Pattern.timestamp.desc()).first()
        recent_locations = Location.query.filter_by(student_id=student_id).order_by(Location.timestamp.desc()).limit(50).all()

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
