from users.data import UsersDB
from users.domain import UsersDomain
from users.presentation import UserPresentation
from utils.constants import DATABASE

"dependency injection инъекция зависимостей"

database = UsersDB(DATABASE)
domain = UsersDomain(database)
presentation = UserPresentation(domain)

