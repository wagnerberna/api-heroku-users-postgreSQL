from flask import Response, request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.model.user import UserModel
from src.service.mail import Mail
from src.service.payload.user import users_ns, user_post_put_fields, token_header
from src.service.message import *


# GetAll
@users_ns.route('users')
class UsersController(Resource):
    def get(self):
        try:
            data_users = UserModel().get_all()

            if data_users == None:
                return USER_NOT_FOUND, 404
            
            # converte todos ids da lista em string
            for user in data_users:
                user['_id'] = str(user['_id'])
                # del user['password']
            return data_users, 200

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
            user_add = UserModel().add(activated, **new_user)
            # id do ítem adicionado
            id = user_add.inserted_id
            print(id)
            
            # envio do email:
            template_path_confirm = 'src/templates/mail_confirm.html'
            email_to = 'wag.backend@gmail.com'
            Mail().send_mail(new_user['login'], new_user['name'], email_to, template_path_confirm)
            
            return {'message': 'user created', 'id': f'{id}'}, 201

        except:
            return INTERNAL_ERROR, 500


# GetById / Update / Delete
@users_ns.route('user/<id>')
class UserController(Resource):
    def get(self, id):
        try:
            data_user = UserModel().get_by_id(id)
            print(data_user)

            if data_user == None:
                return USER_NOT_FOUND, 404
            
            id_db = str(data_user.get('_id'))
            name = data_user.get('name')
            login = data_user.get('login')
            email = data_user.get('email')
            activated = data_user.get('activated')

            if data_user:
                return {'id': id_db, 'name': name, 'login':login, 'email': email, 'activated': activated}, 200

        except:
            return INTERNAL_ERROR, 500

    @users_ns.expect(token_header, user_post_put_fields)
    @jwt_required()
    def put(self, id):
        try:
            data = request.get_json()
            data_update = UserModel().update(id, **data)

            print(request.headers)

            # verificar se foi feito o update pelo atributo de count
            print(data_update.modified_count)
            if data_update.modified_count == 1:
                return UPDATE_SUCCESS, 200
            return NOTHING_UPDATE, 409

        except:
            return INTERNAL_ERROR, 500

    @jwt_required()
    def delete(self, id):
        try:
            data_delete = UserModel().delete(id)

            if data_delete.deleted_count == 1:
                return {'message': 'user delete', 'id': f'{id}'}, 200
            return USER_NOT_FOUND, 404

        except:
            return INTERNAL_ERROR, 500
