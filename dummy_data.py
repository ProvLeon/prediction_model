# prediction_model/dummy_data.py
from app import create_app, db
from app.models import Student, Location
import random
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError


app = create_app()

def create_dummy_data():
    with app.app_context():
        # Create all tables
        db.create_all()

        # Create dummy students
        students = [
            Student(id="COH201708014", name="John Doe", email="john@example.com", phone="1234567890"),
            Student(id="COH201708015", name="Jane Smith", email="jane@example.com", phone="0987654321"),
            Student(id="COH201708016", name="Bob Johnson", email="bob@example.com", phone="1122334455")
        ]

        for student in students:
           try:
               db.session.add(student)
               db.session.flush()
           except IntegrityError:
               db.session.rollback()
               print(f"Student with ID {student.id} or phone {student.phone} already exists. Skipping.")

        # Create dummy locations for each student
        base_lat, base_lon = 40.7128, -74.0060  # New York City coordinates
        start_time = datetime.utcnow() - timedelta(days=7)

        for student in students:
            for i in range(100):
                lat = base_lat + random.uniform(-0.01, 0.01)
                lon = base_lon + random.uniform(-0.01, 0.01)
                timestamp = start_time + timedelta(hours=i)
                location = Location(student_id=student.id, latitude=lat, longitude=lon, timestamp=timestamp)
                db.session.add(location)

        db.session.commit()

if __name__ == "__main__":
    create_dummy_data()
    print("Dummy data created successfully!")
