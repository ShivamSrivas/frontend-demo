# config.py

import os

class Config:
    USER = os.getenv('DB_USER', 'your_user_name')  
    PASSWORD = os.getenv('DB_PASSWORD', 'your_user_password')  
    HOST = os.getenv('DB_HOST', 'your_host')  
    DATABASE = os.getenv('DB_NAME', 'your_database')
    
    SQLALCHEMY_DATABASE_URI = f"mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
