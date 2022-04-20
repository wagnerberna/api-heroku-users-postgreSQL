from flask import request, make_response, render_template
from flask_restx import Resource
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended.utils import get_jwt
from blacklist import BLACKLIST
from src.model.login import LoginModel
from src.service.passwords import compare_password
from src.resources.auth_ns_payload import auth_ns, token_header, login_fields
from src.service.message import *
from src.model.dto.loginDto import LoginDto

login_model = LoginModel()

# Login
@auth_ns.expect(login_fields, validate=True)
class LoginController(Resource):
    def post(self):
        try:
            data = LoginDto.parse_obj(request.get_json())
            login_db = login_model.find_login(data.login)

            if login_db == False:
                return AUTH_FAILED, 409

            check_password = compare_password(data.password, login_db.get("password"))
            if check_password == False:
                return AUTH_FAILED, 409

            if login_db.get("activated") == False:
                return LOGIN_INACTIVE

            token = create_access_token(identity=login_db.get("login"))
            return {"token": token}, 200

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500


# Logout
@auth_ns.expect(token_header)
class LogoutController(Resource):
    @jwt_required()
    def post(self):
        try:
            jwt_id = get_jwt()["jti"]
            BLACKLIST.add(jwt_id)
            return LOGGED_SUCCESSFUL, 200

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500


# confirm Login
class LoginConfirmController(Resource):
    @classmethod
    def get(cls, login):
        try:
            find_login = login_model.find_login(login)

            if not find_login:
                return LOGIN_NOT_FOUND, 404

            status_update = login_model.update_status(login, True)
            if status_update == 0:
                return NOTHING_UPDATE, 409

            # Return alternative in JSON:
            # return LOGIN_CONFIRMED, 200

            # Return in HTML:
            headers = {"Content-Type": "text/html"}
            template_response = make_response(
                render_template("login_confirm.html", login_user=login), 200, headers
            )
            return template_response

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500
