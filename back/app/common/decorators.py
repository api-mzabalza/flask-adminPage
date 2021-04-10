from flask import request, jsonify, current_app

# SCHEMAS
from app.schemas.user import UserSchema
from app.schemas.validators.login import LoginSchema

from app.models.user import User


from functools import wraps
import jwt

# def validator(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         print('yuhuuu')
#         # errors = LoginSchema().validate(request.get_json())
#         # if errors:
#         #     return {'message': 'Error','Error': errors}
#         return f(*args, **kwargs)
#     return decorated


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        bearer = request.headers.get('Authorization')
        if not bearer:
            return jsonify({'message': 'Token is missing'}), 401

        token = bearer.split(' ')[1].strip('"')
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except Exception as e:
            return jsonify({'message': f'Token is invalid: {e}'}), 401

        rtn = User.query.filter_by(id=data['id']).all()

        if not rtn:
            return {'token': False,'message': 'User doesnt exist'}
        loged_user = UserSchema().dump(rtn[0])
        return f(loged_user, *args, **kwargs)

    return decorated

