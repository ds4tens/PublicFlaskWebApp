from flask import Blueprint, request, json
from flaskr.db import MSSQLDB
from .parsetools import parse_req
from flaskr.config import DATABASE_PROCEDURES

bp = Blueprint('webhook', __name__, url_prefix='/webhook')


@bp.route('/', methods=['POST', 'GET'])
def get_webhook():
    # TODO сделать нормальный ответ ответа при ошибке
    # TODO добавить обработку секрета, если его добавят
    # header = dict(request.headers)

    if not request.is_json:
        return json.jsonify({'status': 'error', 'message': 'not json'})

    data = json.loads(request.data)
    with MSSQLDB() as db:
        for i in range(len(data['baskets'])):
            temp_dict = parse_req(data, i)
            db.callproc(DATABASE_PROCEDURES[0], *temp_dict.values())  # передача процедуры и аргументов

    return {"status": "ok"}
