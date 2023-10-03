import logging

from utils.exceptions import *


def handler_exception(e):
    if type(e) is DBException:
        logging.critical(f'Исключение при работе с БД: {e}')
        return e.text, 400
    elif type(e) is DomainException:
        logging.critical(f'Исключение при работе со слоем доменной логики Domain: {e}')
        return e.text, 400
    elif type(e) is ViewException:
        logging.critical(f'Исключение при работе со слоем View: {e}')
        return e.text, 400
    else:
        logging.critical(f'Неожиданное исключение: {e}')
        return e.text, 400

