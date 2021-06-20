import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost/sys'
SQLALCHEMY_TRACK_MODIFICATIONS = False
