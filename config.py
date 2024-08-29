import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///student_tracking.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'ksdfklsjfsljdlfjajladklajdfasdfdklafkakld;fjakjdfl;acuvhnfrf98uadfnqhrafjfsdfasjdfka8olrqjohfasf'
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
