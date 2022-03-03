from flask import Response, request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.model.user import UserModel
from src.service.mail import Mail
from src.service.payload.user import users_ns, user_post_put_fields, token_header
from src.service.message import *

user_model = UserModel()

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
            
            users = []
            print(users)
            for user in data_users:
                user_add = {
                    "user_id": user[0],
                    "name": user[1],
                    "email": user[2],
                    "login": user[3],
                    "password": "******",
                    "status": user[5],
                }
                # print(user_add)
                users.append(user_add)
            
            print(users)

            return users, 200

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
            activated = False
            user_add = user_model.add(activated, **new_user)

            if user_add == 0:
                return USER_NOT_CREATED, 409

            # envio do email:
            template_path_confirm = 'src/templates/mail_confirm.html'
            email_to = 'wag.backend@gmail.com'
            Mail().send_mail(new_user['login'], new_user['name'], email_to, template_path_confirm)

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
            # print(data_user)

            if data_user == None:
                return USER_NOT_FOUND, 404
            
            result = {
                "user_id": data_user[0],
                "name": data_user[1],
                "email": data_user[2],
                "login": data_user[3],
                "password": "******",
                "status": data_user[5],
            }

            # print(result)

            return result, 200

        except:
            return INTERNAL_ERROR, 500

    # @jwt_required()
    @users_ns.expect(token_header, user_post_put_fields)
    def put(self, id):
        try:
            # print("token:::", request.headers)

            data = request.get_json()
            user_update = user_model.update(id, **data)
            print("user_update:::", user_update)

            if user_update == 0:
                return NOTHING_UPDATE, 409
            return UPDATE_SUCCESS, 200

        except:
            return INTERNAL_ERROR, 500

    # @jwt_required()
    def delete(self, id):
        try:
            data_delete = user_model.delete(id)

            if data_delete == 0:
                return USER_NOT_FOUND, 404
            return USER_DELETED, 200

        except:
            return INTERNAL_ERROR, 500
