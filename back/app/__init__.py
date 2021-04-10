from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_restplus import Api, Resource
from flask_restful import Api

from app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
# api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    # api.init_app(app)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    db.init_app(app)
    bcrypt.init_app(app)

    # Routes
    from app.routes.main import blueprint as main
    app.register_blueprint(main, url_prefix='/')

    from app.routes.user import user
    app.register_blueprint(user, url_prefix='/')

    return app