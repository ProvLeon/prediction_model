from app import db
from datetime import datetime

class Student(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.name}>'

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100), db.ForeignKey('student.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100), db.ForeignKey('student.id'), nullable=False)
    pattern_data = db.Column(db.PickleType, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
