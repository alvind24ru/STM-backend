#from tasks.models import Task


class DBException(Exception):
    """Исключение при работе с БД"""
    text: str
    exception: Exception

    def __init__(self, exception: Exception, text: str = ''):
        self.text = text
        self.exception = exception


class TaskException(Exception):
    """Исключения доменной логики domain"""
    text: str

    def __init__(self, text: str = ''):
        self.text = text


class ViewException(Exception):
    """Исключения в Presentation"""

    def __init__(self, text: str = ''):
        self.text = text


class UserException(Exception):
    def __init__(self, text: str = ''):
        self.text = text

