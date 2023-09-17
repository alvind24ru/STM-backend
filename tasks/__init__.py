from . import di
import json
from utils.exceprion_mapper import handler_exception
from utils.constants import VERSION, HEADERS
from utils.flask import *

api = di.presentation


@app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['GET'])
def get_task(taskid):
    try:
        return api.get_task(taskid), 200, HEADERS
    except Exception as e:
        handler_exception(e)


@app.route(f'/api/{VERSION}/test', methods=['GET'])
def test():
    return 'True'
