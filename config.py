import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_SETTINGS = {'host': os.getenv('MONGODB_URI')}
    SECRET_KEY = os.getenv('SECRET_KEY') or 'ksdfklsjfsljdlfjajladklajdfasdfdklafkakld;fjakjdfl;acuvhnfrf98uadfnqhrafjfsdfasjdfka8olrqjohfasf'
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
