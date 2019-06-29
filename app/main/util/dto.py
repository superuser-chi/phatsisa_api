from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'firstname': fields.String(required=True, description='user username'),
        'lastname': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'phone': fields.String(required=True, description='user cellphone number'),
        'public_id': fields.String(description='user Identifier')
    })
    user2 = api.model('user2', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'firstname': fields.String(required=True, description='user username'),
        'lastname': fields.String(required=True, description='user username'),
        'phone': fields.String(required=True, description='user celllphone number'),
        'old_password': fields.String(required=True, description='user password'),
        'password': fields.String(required=True, description='user password'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


