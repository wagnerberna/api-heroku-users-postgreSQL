from flask_restx import fields, Namespace

# Namespaces (conjunto de rotas)
users_ns = Namespace('users_route', description='namespace CRUD for all users')

# payloads
user_post_put_fields = users_ns.model('UserAddFields', {
    'name': fields.String(required=True, help='Name cannot be blank!'),
    'email': fields.String(required=True),
    'login': fields.String(required=True),
    'password': fields.String(required=True)
})

# Headers
token_header = users_ns.parser()
token_header.add_argument('Authorization', location='headers')
