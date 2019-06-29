from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, del_a_user,update_user

api = UserDto.api
_user = UserDto.user
_user2 = UserDto.user2



@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')

    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

    @api.doc('delete a user')
    def delete(self, public_id):
        """delete a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            del_a_user(public_id)
            response_object = {
            'status': 'success',
            'message': 'User successfully deleted.',
            }
            return response_object

    @api.expect(_user2, validate=True)
    @api.doc('update a user')
    def put(self, public_id):
        """update a user given its identifier"""
        
        user = get_a_user(public_id)
        if not user:
            api.abort(405)
        else:
            data = request.json
            return update_user(public_id=public_id,data=data)
            




