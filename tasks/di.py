from . import data
from . import domain
from .presentation import *
from utils.constants import *
from users.di import domain

"dependensy injection инъекция зависимостей"

database = TaskDB(DATABASE_NAME)
task_domain = TaskDomain(database)
user_domain = domain
presentation = TaskPresentation(task_domain, user_domain)

