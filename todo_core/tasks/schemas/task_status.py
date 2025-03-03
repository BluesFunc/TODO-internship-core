from rest_marshmallow import Schema, fields

from tasks.choices import TaskStatus


class TaskStatusSchema(Schema):
    status = fields.Enum(TaskStatus)
