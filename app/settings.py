import os
import sys

from app import app

# SQLite URI compatible
WINDOWS = sys.platform.startswith('win')
if WINDOWS:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


# /data.py
dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
