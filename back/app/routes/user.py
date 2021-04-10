from flask import Blueprint, request, jsonify, current_app
from app import db, bcrypt
from app.common.decorators import token_required
import datetime
import jwt

# SCHEMAS
from app.schemas.user import UserSchema
from app.schemas.validators.login import LoginSchema

# MODELS
from app.models.user import User
from app.models.post import Post

# TODO: Create Serializers to return json data

user = Blueprint('user', __name__)

@user.route("/login", methods=['POST'])
def login():

    errors = LoginSchema().validate(request.get_json())
    if errors:
        return {'message': 'Error','Error': errors}

    params = request.get_json()
    email = params.get('email')
    password = params.get('password')
    rtn = User.query.filter_by(email=email).all()

    if not rtn:
        return {'token': False,'message': 'Wrong Username'}

    user = vars(rtn[0])
    print(user)
    if user and bcrypt.check_password_hash(user['password'], password):
        
        token = jwt.encode({'id': user['id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, current_app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({
            'token': token,
            **UserSchema().dump(user)
        })

    return {
        'token': False,
        'message': 'Wrong Password'
    }

# Create new User
@user.route("/register", methods=['POST'])
def register():
    ## TODO: INPUT VALIDATOR DECORATOR
    data = request.json
    data['password'] = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    newUser = User(**data)
    try:
        db.session.add(newUser)
        db.session.commit()
    except Exception as e:
        error = str(e.__dict__['orig'])
        return {'message': f'Error', 'Error': error}

    return {
        'status': True,
        'message': f"New {data.get('username')} created.",
        'user': UserSchema().dump(newUser)
    }

# Delete user
@token_required
@user.route("/user", methods=['DELETE'])
def delete_user():
    _id = request.get_json()['id']
    try:
        user = User.query.filter(User.id==_id).delete()
        db.session.commit()
    except Exception as e:
        return {'message': f'Error', 'Error': str(e)}
    
    if user:
        return {'status': True, 'message': f'Deleted user with id: {_id}'}
    return {'status': False, 'message': f'User not found for id: {_id}'}


# Get all users
@user.route("/user", methods=['GET'])
@token_required
def get_all_users(loged_user):
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users))


@user.route("/user/<int:user_id>", methods=['GET'])
@token_required
def getUserById(loged_user, user_id):
    # print(user_id)
    rtn = User.query.filter_by(id=user_id).all()
    if not rtn:
        return {
            'status': False,
            'message': 'Wrong user id'
        }

    user = UserSchema().dump(rtn[0])
    
    return {
        'status': True,
        'user': user
    }