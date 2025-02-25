from tasks.models import TaskStatusSubscribers


class TaskStatusSubscriberService:

    @staticmethod
    def create(entity: TaskStatusSubscribers) -> TaskStatusSubscribers:
        entity.save()
        return entity
