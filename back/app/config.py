import os

class Config:
    # SECRET_KEY = '5dff52b8ac26ff40b60afb0fb07e4e22'
    # SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
