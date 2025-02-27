from datetime import datetime

from tasks.models import Task


class TaskService:

    @staticmethod
    def set_deadline(task: Task, deadline: datetime) -> None:
        task.deadline = deadline
        task.save()
