from rest_marshmallow import Schema, fields


class TaskDeadlineSchema(Schema):
    deadline = fields.DateTime(format="iso")
