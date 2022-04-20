from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from src.resources.auth_ns_payload import auth_ns
from src.resources.user_ns_payload import users_ns, user_ns
from src.controller.login import (
    LoginController,
    LogoutController,
    LoginConfirmController,
)
from src.controller.user import UsersController, UserController, UserAddController
from blacklist import BLACKLIST
import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = os.getenv("APP_PORT")
APP_DEV_CONFIG = os.getenv("APP_DEV")
APP_PROD_CONFIG = os.getenv("APP_PROD")

app = Flask(__name__, template_folder="src/templates")

app.config.from_object(APP_DEV_CONFIG)

api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def verifify_blacklist(self, token):
    print(BLACKLIST)
    print(token)
    print(token["jti"] in BLACKLIST)
    return token["jti"] in BLACKLIST


api.add_namespace(users_ns)
api.add_namespace(user_ns)
api.add_namespace(auth_ns)

auth_ns.add_resource(LoginController, "/login")
auth_ns.add_resource(LogoutController, "/logout")
auth_ns.add_resource(LoginConfirmController, "/confirm/<login>")

users_ns.add_resource(UsersController, "")
user_ns.add_resource(UserController, "/<id>")
user_ns.add_resource(UserAddController, "")


# comment to send to heroku
if __name__ == "__main__":
    app.run(port=APP_PORT or 5000)
