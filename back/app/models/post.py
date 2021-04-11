from app import db, admin
from datetime import datetime
from flask_admin.contrib.sqla import ModelView


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class PostView(ModelView):
    column_list = ['id','title', 'date_posted', 'content', 'user_id']
    # olumn_searchable_list = ["title"]

# admin.add_view(PostView(Post, db.session, list_columns=['id', 'title', 'date_posted', 'content', 'user_id']))
admin.add_view(PostView(Post, db.session))
