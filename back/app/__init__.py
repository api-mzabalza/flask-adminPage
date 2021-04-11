from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_restplus import Api, Resource
from flask_restful import Api
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
admin = Admin(template_mode='bootstrap3')
# admin = Admin()
# api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    # api.init_app(app)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False

    # Init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)

    # from app.models.user import User


    # admin.add_view(ModelView(User, db.session))
    # admin.add_view(MyView(name='MyCustomView', endpoint='db'))

    # Routes
    from app.routes.main import blueprint as main
    app.register_blueprint(main, url_prefix='/')

    from app.routes.user import blueprint as user_b
    app.register_blueprint(user_b, url_prefix='/')

    return app