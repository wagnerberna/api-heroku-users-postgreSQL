from flask import request, make_response, render_template
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended.utils import get_jwt
from blacklist import BLACKLIST
from src.model.login import LoginModel
from src.core.login import LoginCore
from src.core.payload.login import login_ns, token_header, login_fields
from src.service.message import *

# instanciar loginmodel
login_model = LoginModel()
login_core = LoginCore()


# Login
@login_ns.route('login')
@login_ns.expect(login_fields)
class LoginController(Resource):
    def post(self):
        try:
            data = request.get_json()
            login_received = data.get('login')
            password_received = data.get('password')

            login_db = login_core.find_login(login_received)
            # print(login_db)
            if login_db == False:
                return AUTH_FAILED, 409

            check_password = login_core.check_password(login_db.get('password'), password_received)
            # print(check_password)
            if check_password == False:
                return AUTH_FAILED, 409

            if login_db.get('activated') == False:
                return LOGIN_INACTIVE

            token = login_core.create_token(login_db.get('login'))
            return {'token': token}, 200

        except:
            return INTERNAL_ERROR, 500


# Logout
# jti (JWT Token Identifier - identificado do token (id))
@login_ns.route('logout')
@login_ns.expect(token_header)
class LogoutController(Resource):
    @jwt_required()
    def post(self):
        try:
            jwt_id = get_jwt()['jti']
            BLACKLIST.add(jwt_id)
            return LOGGED_SUCCESSFUL, 200

        except:
            return INTERNAL_ERROR, 500


@login_ns.route('confirm/<login>')
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

            # retorno JSON:
            # return LOGIN_CONFIRMED, 200

            # retorno HTML: (Passa um headers p/ não interpretar como json):
            # make / render (flask busca por padrão na pasta templates setar no app)
            headers = {'Content-Type': 'text/html'}
            template_response = make_response(render_template('login_confirm.html', login_user=login), 200, headers)
            return template_response

        except:
            return INTERNAL_ERROR, 500
