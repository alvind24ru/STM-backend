import logging

from utils.exceptions import *


def handler_exception(e: Exception):
    if type(e) is DBException:
        logging.critical(f'Исключение при работе с БД: {e}')
        return e, 400
    elif type(e) is TaskException:
        logging.critical(f'Исключение при работе со слоем доменной логики Domain задач: {e}')
        return e, 400
    elif type(e) is UserException:
        logging.critical(f'Исключение при работе со слоем доменной логики Domain пользователей: {e}')
        return e, 400
    else:
        logging.critical(f'Неожиданное исключение: {e}')
        return e, 400
