"""Описание кастомных исключений"""


class DBException(Exception):
    """Исключение при работе с БД"""

    def __init__(self, exception: Exception, text: str = ''):
        self.text = text
        self.exception = exception


class DomainException(Exception):
    """Исключения доменной логики domain"""

    def __init__(self, text: str = ''):
        self.text = text


class ViewException(Exception):
    """Исключения в Presentation"""

    def __init__(self, text: str = ''):
        self.text = text

