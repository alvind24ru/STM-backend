from tasks.presentation import *
from utils.constants import *
from users.di import domain

"dependency injection инъекция зависимостей"

database = TaskDB(DATABASE_PATH)
task_domain = TaskDomain(database)
user_domain = domain
presentation = TaskPresentation(task_domain, user_domain)

