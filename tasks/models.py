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



