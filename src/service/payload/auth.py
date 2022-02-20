from flask_restx import fields, Namespace

# Namespaces (conjunto de rotas)
auth_ns = Namespace('auth_route', description='namespace for login and logout')

# payloads
auth_login_fields = auth_ns.model('AuthLoginFields', {
    'login': fields.String(required=True),
    'password': fields.String(required=True)
})

# Headers
token_header = auth_ns.parser()
token_header.add_argument('Authorization', location='headers')