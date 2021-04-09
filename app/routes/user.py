from flask import Blueprint, request, flash, render_template, url_for, redirect
from app.forms import RegistrationForm, LoginForm
from app import db

# MODELS
from app.models.user import User

user = Blueprint('user', __name__)

@user.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', title="Login", form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password!', 'danger')

        return render_template('login.html', title="Login", form=form)


@user.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('register.html', title="Register", form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        flash(f'Account failed for {form.username.data}!', 'danger')
        return render_template('register.html', title="Register", form=form)


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