from flask import Blueprint, request, jsonify, current_app
from app import db, bcrypt
from app.common.decorators import token_required
import datetime
import jwt

# MODELS
from app.models.user import User
from app.models.post import Post

# TODO: Create Serializers to return json data

post = Blueprint('_post', __name__)

# # Create POST
# @post.route('/post', methods=['POST'])
# @token_required