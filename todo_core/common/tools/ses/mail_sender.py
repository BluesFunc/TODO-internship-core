from projects.models import Project
from tasks.models import Task


class MailSender:
    @staticmethod
    def send_change_deadline_notification(mail: str, task: Task) -> None:
        pass

    @staticmethod
    def send_project_invitation_message(mail: str, project: Project) -> None:
        pass

    @staticmethod
    def send_subscribe_notification(mail: str, task: Task) -> None:
        pass

    @staticmethod
    def send_unsubscribe_message(mail: str, task: Task) -> None:
        pass
