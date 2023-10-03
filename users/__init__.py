#from users.di import *
from flask import request

from users.di import presentation
from utils.exceprion_mapper import handler_exception
from utils.constants import VERSION, HEADERS
from utils.flask import app


api = di.presentation


@app.route(f'/api/{VERSION}/users/', methods=['POST', 'GET'])
def create_user():
    try:
        return api.create_user(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/<int:userid>', methods=['GET'])
def get_user(userid):
    try:
        return api.get_user(userid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/', methods=['PATCH'])
def update_user():
    try:
        return api.update_user(request.args), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/<int:userid>', methods=['DELETE'])
def delete_user(userid):
    try:
        return api.delete_user(userid), 200, HEADERS
    except Exception as e:
        return handler_exception(e)


@app.route(f'/api/{VERSION}/users/get-all', methods=['GET'])
def get_all_users():
    try:
        return api.get_all_users(), 200, HEADERS
    except Exception as e:
        return handler_exception(e)
