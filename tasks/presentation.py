from tasks.domain import *
from tasks.models import *
from users.domain import UsersDomain

TASKID = 'id'
USERNAME = 'username'
TITLE = 'title'
DESCRIPTION = "description"
DONE = 'done'


class TaskPresentation:
    """Описывается вся логика"""
    __domain: TaskDomain
    __users_domain: UsersDomain

    def __init__(self, domain: TaskDomain, user_domain: UsersDomain):
        self.__domain = domain
        self.__users_domain = user_domain

    def get_task(self, taskid: int) -> str:
        task = self.__domain.get_task(taskid)
        return self.__task_to_json(task)

    def create_task(self, args) -> str:
        if USERNAME in args and TITLE in args and DESCRIPTION in args and DONE in args:
            task = self.__domain.create_task(Task(None, args[USERNAME], args[TITLE], args[DESCRIPTION], args[DONE]))
            return self.__task_to_json(task)
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def update_task(self, args) -> str:
        if TASKID and USERNAME and TITLE and DESCRIPTION and DONE in args:
            task = self.__domain.update_tasks(self.__args_to_task_object(args))
            return self.__task_to_json(task)
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def delete_task(self, taskid: int) -> str:
        return self.__domain.delete_tasks(taskid)

    def get_all_user_tasks(self, userid: int) -> list:
        self.__users_domain.check_user_id_or_except(userid)
        return self.__domain.get_all_user_tasks(userid)

    @staticmethod
    def __task_to_json(task: Task) -> str:
        return f"""{{"{TASKID}": {task.id},
        "{USERNAME}": "{task.username}",
        "{TITLE}": "{task.title}",
        "{DESCRIPTION}": "{task.description}",
        "{DONE}": "{task.done}"}}"""

    @staticmethod
    def __args_to_task_object(args) -> Task:
        return Task(args['id'], args['username'], args['title'], args['description'], args['done'])
