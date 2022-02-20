from flask import request, make_response, render_template
from flask_restx import Resource
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended.utils import get_jwt
from blacklist import BLACKLIST
from werkzeug.security import safe_str_cmp
from src.model.auth import AuthModel
from src.service.payload.auth import auth_ns, token_header, auth_login_fields
from src.service.message import *

# instanciar authmodel
auth_model = AuthModel()

# Login
@auth_ns.route('login')
@auth_ns.expect(auth_login_fields)
class LoginController(Resource):
    def post(self):
        try:
            data = request.get_json()
            login = data.get('login')
            password = data.get('password')

            login = auth_model.find_login(login)
            print(login)

            if login['activated'] == False:
                return LOGIN_INACTIVE

            # se existir um user e a senha for igual
            # safe método seguro de comparar string de password
            # token gerado baseado no login
            if login != None and safe_str_cmp(login['password'], password):
                id = str(login.get('_id'))
                token = create_access_token(identity=id)
                return {'token': token}, 200

            return AUTH_FAILED, 409
        except:
            return INTERNAL_ERROR, 500


# Logout
# jti (JWT Token Identifier - identificado do token (id))
@auth_ns.route('logout')
@auth_ns.expect(token_header)
class UserLogout(Resource):
    @jwt_required()
    def post(self):
        try:
            jwt_id = get_jwt()['jti']
            BLACKLIST.add(jwt_id)
            return LOGGED_SUCCESSFUL, 200

        except:
            return INTERNAL_ERROR, 500


@auth_ns.route('confirm/<login>')
class LoginConfirm(Resource):
    @classmethod
    def get(cls, login):
        try:
            find_login = auth_model.find_login(login)

            if not find_login:
                return LOGIN_NOT_FOUND, 404

            status_update = auth_model.update_status(login, True)
            if status_update.modified_count == 1:

                # retorno JSON:
                # return LOGIN_CONFIRMED, 200

                # retorno HTML: (Passa um sheaders p/ não interpretar como json):
                # make / render (flask busca por padrão na pasta templates setar no app)
                headers = {'Content-Type': 'text/html'}
                template_response = make_response(
                    render_template('login_confirm.html', login_user=login), 200, headers
                )
                return template_response

            return NOTHING_UPDATE, 409

        except:
            return INTERNAL_ERROR, 500
