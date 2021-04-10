from marshmallow import Schema, fields

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    date_posted = fields.DateTime()
    user_id = fields.Int()


post_schema = PostSchema(many=True)