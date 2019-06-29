import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['phone']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            phone=data['phone'],
            password=data['password'],
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def update_user(public_id,data):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exists',
        }
        return response_object, 404
    else:
        if user.check_password(data['old_password']):
            user.email = data['email']
            user.username = data['username']
            user.firstname=data['firstname']
            user.lastname=data['lastname']
            user.password = data['password']
            user.phone = data['phone']
            db.session.merge(user)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'User successfully updated',
            }
            return response_object, 200
        else:
            response_object = {
            'status': 'fail',
            'message': 'User password does not match',
            }
            return response_object, 404 


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

def del_a_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    db.session.delete(user)
    db.session.commit()




def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

