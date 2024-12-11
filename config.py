

import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin%40123@localhost/inventory_mgmt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SECURE = True 
    SESSION_COOKIE_HTTPONLY = True  
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30) 