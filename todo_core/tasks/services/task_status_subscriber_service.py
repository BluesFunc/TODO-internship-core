from uuid import UUID

from tasks.models import Task, TaskStatusSubscribers


class TaskStatusSubscriberService:

    @staticmethod
    def create(model: TaskStatusSubscribers) -> TaskStatusSubscribers:
        model.save()
        return model

    @staticmethod
    def delete(task: Task, user_id: UUID) -> None:
        TaskStatusSubscribers.objects.get(task_id=task, user_id=user_id).delete()
