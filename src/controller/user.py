from flask import Response, request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.model.user import UserModel
from src.service.mail import Mail
from src.core.user import UserCore
from src.core.payload.user import users_ns, user_post_put_fields, token_header
from src.service.message import *

user_model = UserModel()
user_core = UserCore()

# GetAll
@users_ns.route('users')
class UsersController(Resource):
    def get(self):
        try:
            # recebe uma lista com tuplas
            data_users = user_model.get_all()
            # print(data_users)

            if data_users == None:
                return USER_NOT_FOUND, 404

            payload_users = []

            for user in data_users:
                payload_user = user_core.payload_get_user(*user)
                payload_users.append(payload_user)

            # print(payload_users)
            return payload_users, 200

        except:
            return INTERNAL_ERROR, 500


# Post
@users_ns.route('useradd')
class UserAddController(Resource):
    @users_ns.expect(user_post_put_fields)
    def post(self):
        try:
            new_user = request.get_json()
            # print(new_user)
            payload = user_core.payload_new_and_update_user(**new_user)
            print('---payload:::', payload)

            if user_core.check_login(payload['login']):
                return LOGIN_ALREDY_EXISTS, 409

            user_add = user_model.add(**payload)
            if user_add == 0:
                return USER_NOT_CREATED, 409

            # envio do email:
            template_path_confirm = 'src/templates/mail_confirm.html'
            Mail().send_mail(payload['login'], payload['name'], payload['email'], template_path_confirm)

            return USER_CREATED, 201

        except:
            return INTERNAL_ERROR, 500


# GetById / Update / Delete
@users_ns.route('user/<id>')
class UserController(Resource):
    def get(self, id):
        try:
            # retorna uma tupla
            data_user = user_model.get_by_id(id)
            print(data_user)

            if data_user == None:
                return USER_NOT_FOUND, 404

            payload = user_core.payload_get_user(*data_user)

            return payload, 200

        except:
            return INTERNAL_ERROR, 500

    # @jwt_required()
    @users_ns.expect(token_header, user_post_put_fields)
    def put(self, id):
        try:
            # print("token:::", request.headers)

            data = request.get_json()
            payload = user_core.payload_new_and_update_user(**data)
            user_update = user_model.update(id, **payload)
            # print("user_update:::", user_update)

            if user_update == 0:
                return NOTHING_UPDATE, 409
            return UPDATE_SUCCESS, 200

        except:
            return INTERNAL_ERROR, 500

    @jwt_required()
    def delete(self, id):
        try:
            data_delete = user_model.delete(id)

            if data_delete == 0:
                return USER_NOT_FOUND, 404
            return USER_DELETED, 200

        except:
            return INTERNAL_ERROR, 500
