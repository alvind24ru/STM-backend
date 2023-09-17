from users.data import UsersDB
from users.domain import UsersDomain
from users.presentation import UserPresentation
from utils.constants import DATABASE_NAME

database = UsersDB(DATABASE_NAME)
domain = UsersDomain(database)
presentation = UserPresentation(domain)

