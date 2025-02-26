from tasks.models import TaskStatusSubscribers


class TaskStatusSubscriberService:

    @staticmethod
    def create(model: TaskStatusSubscribers) -> TaskStatusSubscribers:
        model.save()
        return model
