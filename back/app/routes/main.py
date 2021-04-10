from flask import Blueprint, render_template
from flask_restful import Api, Resource


# Example to test functionalities of Flask-restful | Flask-restplus

blueprint = Blueprint('main', __name__)
api = Api(blueprint)

posts = [
    {
        'author': 'Mikel Zabalza',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
]

class Main(Resource):
    def get(self):
        return {
            'status': True,
            'message': 'Wellcome to the api'
        }

api.add_resource(Main, '/')