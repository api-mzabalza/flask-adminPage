from flask import Blueprint, render_template

main = Blueprint('main', __name__)

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

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', posts=posts)
    # return 'yuhuuu'

@main.route("/about")
def about():
    return render_template('about.html', title="About")