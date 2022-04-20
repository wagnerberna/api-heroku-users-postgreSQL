from flask_restx import fields, Namespace

# Namespaces
auth_ns = Namespace(
    "auth", description="Route for authentication: login, logout and confirm login"
)

# payloads
login_fields = auth_ns.model(
    "AuthLoginFields",
    {"login": fields.String(required=True), "password": fields.String(required=True)},
    strict=True,
)

# Headers
token_header = auth_ns.parser()
token_header.add_argument("Authorization", location="headers")
