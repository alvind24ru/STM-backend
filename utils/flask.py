from flask import Flask

from . import constants

app = Flask(constants.APP_NAME)
