from flask import Blueprint, request
from app import db, bcrypt
from app.models.user import User
from app.models.post import Post

# MODELS
from app.models.user import User

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
        return {
            'status': True,
            'message': 'Building login endpoint...'
        }
        

# Get all users
@user.route("/user", methods=['GET'])
def getAll():
    '''
    Gell all users
    '''
    users = User.query.all()
    print(users)
    return {
        'status': True,
        'data': users
    }

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