import os
import psycopg2
import datetime
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# Classe pai
# remover do app.run o debug=true
class Config:
    # config Token
    DEBUG = True
    TESTING = True
    JWT_SECRET_KEY = JWT_SECRET_KEY
    JWT_BLACKLIST_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=2)
    # JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)

# classes de produção e teste
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

# https://hackersandslackers.com/configure-flask-applications/