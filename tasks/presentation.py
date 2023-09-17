from tasks.domain import *
from tasks.models import *

TASKID = 'id'
USERNAME = 'username'
TITLE = 'title'
DESCRIPTION = "description"
DONE = 'done'


class TaskPresentation:
    """Описывается вся логика"""
    __domain: TaskDomain

    def __init__(self, domain: TaskDomain):
        self.__domain = domain

    def get_task(self, taskid: int) -> str:
        task = self.__domain.get_task(taskid)
        return self.__task_to_json(task)

    def create_task(self, args) -> str:
        if USERNAME in args and TITLE in args and DESCRIPTION in args and DONE in args:
            task = self.__domain.create_task(self.__args_to_task_object(args))
            return self.__task_to_json(task)
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def update_task(self, args) -> str:
        # TODO Правильно ли проверять в presentation
        if USERNAME in args and TITLE in args and DESCRIPTION in args and DONE in args:
            task = self.__domain.update_tasks(self.__args_to_task_object(args))
            return self.__task_to_json(task)
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def delete_task(self, taskid: int) -> str:
        return self.__domain.delete_tasks(taskid)



    def get_all_user_tasks(self) -> str:
        return self.__domain.get_all_user_tasks()

    @staticmethod
    def __task_to_json(task: Task) -> str:
        return f"""{{"{TASKID}": {task.id},
        "{USERNAME}": "{task.username}",
        "{TITLE}": "{task.title}",
        "{DESCRIPTION}": "{task.description}",
        "{DONE}": "{task.done}"}}"""

    @staticmethod
    def __args_to_task_object(args) -> Task:
        return Task(None, args['username'], args['title'], args['description'], args['done'])


