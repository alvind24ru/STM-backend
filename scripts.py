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
