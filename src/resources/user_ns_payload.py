from flask_restx import fields, Namespace


# Namespaces
users_ns = Namespace("users", description="Route for list all users")

user_ns = Namespace("user", description="Route for CRUD for user")


# payloads
user_post_fields = user_ns.model(
    "UserAddFields",
    {
        "name": fields.String(required=True, help="Name cannot be blank!"),
        "age": fields.Integer(required=False),
        "email": fields.String(required=True, help="Name cannot be blank!"),
        "city": fields.String(required=False),
        "login": fields.String(required=True, help="Name cannot be blank!"),
        "password": fields.String(required=True, help="Name cannot be blank!"),
        "description": fields.String(required=False),
        "activated": fields.String(Require=False),
    },
)

user_put_fields = user_ns.model(
    "UserUpdateFields",
    {
        "name": fields.String(required=False),
        "age": fields.Integer(required=False),
        "email": fields.String(required=False),
        "city": fields.String(required=False),
        "description": fields.String(required=False),
        "activated": fields.String(Require=False),
    },
)

# Headers
token_header = user_ns.parser()
token_header.add_argument("Authorization", location="headers")
