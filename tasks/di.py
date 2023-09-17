from . import data
from . import domain
from .presentation import *
from utils.constants import *

database = TaskDB(DATABASE_NAME)
task_domain = TaskDomain(database)
presentation = TaskApi(task_domain)
