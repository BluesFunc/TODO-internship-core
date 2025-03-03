from datetime import datetime

from tasks.choices import TaskStatus
from tasks.models import Task


class TaskService:

    @staticmethod
    def set_deadline(task: Task, deadline: datetime) -> None:
        task.deadline = deadline
        task.save()

    @staticmethod
    def set_status(task: Task, status: str) -> None:
        task.status = TaskStatus[status].value
        task.save()
