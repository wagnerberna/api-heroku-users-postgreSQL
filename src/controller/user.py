from flask import Response, request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.model.user import UserModel
from src.model.login import LoginModel
from src.service.mail import Mail
from src.core.user import UserCore
from src.resources.user_ns_payload import (
    user_ns,
    user_post_fields,
    user_put_fields,
    token_header,
)
from src.service.message import *
from src.model.dto.userDto import UserDtoAdd, UserDtoUpdate

user_model = UserModel()
login_model = LoginModel()
user_core = UserCore()

# GetAll
class UsersController(Resource):
    def get(self):
        try:
            payload_users = user_model.get_all()

            if payload_users == None:
                return USER_NOT_FOUND, 404
            return payload_users, 200

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500


# Post
class UserAddController(Resource):
    @user_ns.expect(user_post_fields)
    def post(self):
        try:
            new_user = UserDtoAdd.parse_obj(request.get_json())
            payload = user_core.payload_new_user(new_user)

            if login_model.find_login(payload.login):
                return LOGIN_ALREDY_EXISTS, 409

            user_add = user_model.add(payload)
            if user_add == 0:
                return USER_NOT_CREATED, 409

            # send mail:
            template_path_confirm = "src/templates/mail_confirm.html"
            Mail().send_mail(
                payload.login,
                payload.name,
                payload.email,
                template_path_confirm,
            )

            return USER_CREATED, 201

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500


# GetById / Update / Delete
class UserController(Resource):
    def get(self, id):
        try:
            data_user = user_model.get_by_id(id)

            if data_user == None:
                return USER_NOT_FOUND, 404

            data_user.password = "********"
            payload_user = data_user.dict()
            return payload_user, 200

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500

    @jwt_required()
    @user_ns.expect(token_header, user_put_fields)
    def put(self, id):
        try:
            data = UserDtoUpdate.parse_obj(request.get_json())
            payload = user_core.payload_update_user(data)
            user_update = user_model.update(id, payload)

            if user_update == 0:
                return NOTHING_UPDATE, 409
            return UPDATE_SUCCESS, 200

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500

    @jwt_required()
    @user_ns.expect(token_header, user_put_fields)
    def delete(self, id):
        try:
            data_delete = user_model.delete(id)

            if data_delete == 0:
                return USER_NOT_FOUND, 404
            return USER_DELETED, 200

        except Exception as error:
            print(error)
            return INTERNAL_ERROR, 500
