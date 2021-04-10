from marshmallow import fields, Schema
from app.schemas.post import post_schema, PostSchema

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    posts = fields.Nested(post_schema)



class UserRegistrationSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    image_file = fields.Str()
    posts = fields.Nested(PostSchema)


user_registration_schema = UserRegistrationSchema(many=True)

# user_schema = UserSchema()