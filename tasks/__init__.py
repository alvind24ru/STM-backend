# import tasks.presentation
from tasks import di
import json
from flask import request
from utils.exceprion_mapper import handler_exception
from utils.constants import VERSION, HEADERS
from utils.flask import app
from tasks import *
from . import data
from . import domain
from .presentation import *
from utils.constants import *

api = di.presentation


@app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['GET'])
def get_task(taskid):
    try:
        return api.get_task(taskid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/', methods=['POST'])
def create_task():
    try:
        return api.create_task(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/', methods=['PATCH'])
def update_task():
    try:
        return api.update_task(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['DELETE'])
def delete_task(taskid):
    try:
        return api.delete_task(taskid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/all/<int:userid>', methods=['GET'])
def get_all_user_tasks(userid):
    try:
        return api.get_all_user_tasks(userid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)