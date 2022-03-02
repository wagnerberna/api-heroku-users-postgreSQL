import os
import psycopg2
import datetime
from dotenv import load_dotenv

load_dotenv()


# Classe pai
# remover do app.run o debug=true
class Config:
    # config Token
    DEBUG = True
    TESTING = True
    JWT_SECRET_KEY = "Udemy!"
    JWT_BLACKLIST_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=2)
    # JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)

# classes de produção e teste
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = "postgres://ndxyrolnkefpxf:cc9f341cfcf4f8b076ee282ecb88872fe9578fa8c53ed495ff15ea6663178a8d@ec2-52-45-83-163.compute-1.amazonaws.com:5432/dbvld7vgp4pomg"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@localhost:5432/wb_db"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

# https://hackersandslackers.com/configure-flask-applications/