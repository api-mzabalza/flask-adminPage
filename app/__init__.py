from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    db.init_app(app)

    # Routes
    from app.routes.main import main
    app.register_blueprint(main, url_prefix='/')

    from app.routes.user import user
    app.register_blueprint(user, url_prefix='/')

    return app