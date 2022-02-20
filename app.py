from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from src.controller.user import users_ns
from src.controller.auth import auth_ns
from blacklist import BLACKLIST
import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = os.getenv("APP_PORT")
APP_DEV_CONFIG = os.getenv("APP_DEV")
# APP_PROD sem usar o .env
APP_PROD_CONFIG = 'config.ProdConfig'

app = Flask(__name__, template_folder='src/templates')

# env:
app.config.from_object(APP_PROD_CONFIG)


api = Api(app)
jwt = JWTManager(app)

# Verifica se o token está na blacklist
# True retorna revogado
@jwt.token_in_blocklist_loader
def verifify_blacklist(self, token):
    print(BLACKLIST)
    print(token)
    print(token["jti"] in BLACKLIST)
    return token["jti"] in BLACKLIST


api.add_namespace(users_ns, path='/')
api.add_namespace(auth_ns, path='/')


# if __name__ == '__main__':
#     app.run(port=APP_PORT or 5000)
