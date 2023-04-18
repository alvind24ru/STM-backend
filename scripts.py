import json


def list_to_json(cur, data: list):
    """Преобразует входные данные вида cursor и list данных в json словарь"""
    result = []
    keys = []
    for column_id, col in enumerate(cur.description):
        keys.append(col[0])
    for i in data:
        d = dict(zip(keys, i))
        result.append(d)
    r = json.dumps(result, ensure_ascii=False)
    return r


# r = [{"taskid": 1, "username": "test_user", "title": "test_title", "description": "test_desc1", "done": "FALSE"},
#      {"taskid": 2, "username": "test_user", "title": "test_title", "description": "test_desc1", "done": "FALSE"},
#      {"taskid": 3, "username": "test_user", "title": "test_title", "description": "test_desc1", "done": "FALSE"},
#      {"taskid": 10, "username": "test_user", "title": "test_title", "description": "test_desc1", "done": "FALSE"},
#      {"taskid": 11, "username": "test_user", "title": "test_title", "description": "test_desc1", "done": "FALSE"},
#      {"taskid": 12, "username": "test_user", "title": "test_title", "description": "test_desc1", "done": "FALSE"}]
# print(type(r[1]))
# print(r[1])
# j = json.dumps(r[1])
# print(type(j))
# print(j)
# d = json.loads(j)
# print(type(d))
# print(d)
