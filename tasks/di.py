from . import data
from . import domain
from .presentation import *
from utils.constants import *

"dependensy injection инъекция зависимостей"

database = TaskDB(DATABASE_NAME)
task_domain = TaskDomain(database)
presentation = TaskPresentation(task_domain)

