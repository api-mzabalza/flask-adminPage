from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models.user import User
from app.models.post import Post
import json

# MODELS
from app.models.user import User

# TODO: Create Serializers to return json data

user = Blueprint('user', __name__)

@user.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return {
            'status': True,
            'message': 'Building login endpoint...'
        }


@user.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        ## TODO: INPUT VALIDATOR DECORATOR
        data = request.json
        hashed_password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        newUser = User(
            username=data.get('username'),
            email=data.get('email'),
            password=hashed_password
        )
        db.session.add(newUser)
        db.session.commit()
        # print(rtn)
        return {
            'status': True,
            'message': f"New {data.get('username')} created."
        }
    return {
        'status': False,
        'message': f'Request method: {request.method} not valid'
    }
        

# Get all users
@user.route("/user", methods=['GET'])
def getAll():
    users = [vars(x) for x in User.get_all()]
    
    formated_users = [{
        'username': x.get('username'),
        'email': x.get('email'),
    } for x in users]

    return jsonify(formated_users)



# Create user
@user.route("/user", methods=['POST'])
def post_user():
    '''
    creat user
    '''

    name = request.get_json()['name']
    email = request.get_json()['email']
    phone = request.get_json()['phone']
    password = request.get_json()['password']
    
    newUser = User(
        username = 1,
        toner_color = 'blue',
        toner_hex = '#0F85FF'
    )


    try:
        db.session.add(newUser)
        db.session.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return {'message': f'Error', 'Error': error}

    return {
        'status': True,
        'message': 'user created'
    }