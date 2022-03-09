from flask_restx import fields, Namespace

# Namespaces (conjunto de rotas)
login_ns = Namespace('auth_route', description='namespace for login and logout')

# payloads
login_fields = login_ns.model('AuthLoginFields', {
    'login': fields.String(required=True),
    'password': fields.String(required=True)
})

# Headers
token_header = login_ns.parser()
token_header.add_argument('Authorization', location='headers')