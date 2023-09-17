class Task:
    def __init__(self, taskid: int = None, username: str = None, title: str = None, description: str = None,
                 done: bool = None):
        self.id = taskid
        self.username = username
        self.description = description
        self.title = title
        self.done = done

    id: int
    username: str
    title: str
    description: str
    done: bool


class User:
    def __init__(self, userid: int = None, username: str = None):
        self.userid = userid
        self.username = username

    userid: int
    username: str
