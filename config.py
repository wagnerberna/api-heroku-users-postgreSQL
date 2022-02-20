import datetime

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

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

# https://hackersandslackers.com/configure-flask-applications/