# Flask_app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from file.env
load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'file.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/nettrafficguard'
