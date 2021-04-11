from app import db, admin
from app.models.post import Post
from flask_admin.contrib.sqla import ModelView


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class UserView(ModelView):
    column_list = ['id','username', 'email', 'image_file', 'password', 'posts']

    # can_delete = False  # disable model deletion

# admin.add_view(PostView(Post, db.session, list_columns=['id', 'title', 'date_posted', 'content', 'user_id']))
admin.add_view(UserView(User, db.session))



# admin.add_view(ModelView(User, db.session))

