def handler_exception(e: Exception): # TODO Сначала логгировать
    if type(e) == DBException:
        return e.text, 400
    if type(e) == TaskException:
        pass
