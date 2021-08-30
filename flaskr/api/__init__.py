from flask import Blueprint
from flask_restful import Api

blu_api = Blueprint('apI', __name__, url_prefix='/api/v1')  # БП и ссылка обращения

api = Api(blu_api)

from flaskr.api.v1 import api_get

api_get()  # вызов к функции работающей с api
