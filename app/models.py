from app import db
from datetime import datetime

class Student(db.Document):
    id = db.StringField(primary_key=True)
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    phone = db.StringField(required=True, unique=True)
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.name}>'

class Location(db.Document):
    student_id = db.ReferenceField(Student, required=True)
    latitude = db.FloatField(required=True)
    longitude = db.FloatField(required=True)
    timestamp = db.DateTimeField(default=datetime.utcnow)

class Pattern(db.Document):
    student_id = db.ReferenceField(Student, required=True)
    pattern_data = db.ListField(db.FloatField(), required=True)
