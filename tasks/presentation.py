from tasks.domain import *

TASKID = 'id'
USERNAME = 'username'
TITLE = 'title'
DESCRIPTION = "description"
DONE = 'done'


class TaskApi:
    """Описывается вся логика"""
    __domain: TaskDomain

    def __init__(self, domain: TaskDomain):
        self.__domain = domain

    def get_task(self, taskid: int) -> str:
        task = self.__domain.get_task(taskid)
        return self.__task_to_json(task)

    @staticmethod
    def __task_to_json(task: Task) -> str:
        return f"""{{"{TASKID}": {task.id},
        "{USERNAME}": "{task.username}",
        "{TITLE}": "{task.title}",
        "{DESCRIPTION}": "{task.description}",
        "{DONE}": "{task.done}"}}"""
