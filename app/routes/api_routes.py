from flask import request
from app.controllers.api.api_controller import api_controller
from app.config import VERSION
from app.main import app


@app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['GET'])
def get_task(taskid):
    try:
        return api_controller.get_task(taskid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/', methods=['POST'])
def create_task():
    try:
        return api_controller.create_task(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/', methods=['PATCH'])
def update_task():
    try:
        return api_controller.update_task(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['DELETE'])
def delete_task(taskid):
    try:
        return api_controller.delete_task(taskid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/tasks/all/<int:userid>', methods=['GET'])
def get_all_user_tasks(userid):
    try:
        return api_controller.get_all_user_tasks(userid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/', methods=['POST', 'GET'])
def create_user():
    try:
        return api_controller.create_user(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/<int:userid>', methods=['GET'])
def get_user(userid):
    try:
        return api_controller.get_user(userid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/', methods=['PATCH'])
def update_user():
    try:
        return api_controller.update_user(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/<int:userid>', methods=['DELETE'])
def delete_user(userid):
    try:
        return api_controller.delete_user(userid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/get-all', methods=['GET'])
def get_all_users():
    try:
        return api_controller.get_all_users(), 200, HEADERS
    except Exception as e:
        return handler_exception(e)
