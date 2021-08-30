from flask_restful import Resource, request
from flask import json
from flaskr.db import MSSQLDB
from flaskr.parsetools import parse_api_req


class SeatingChart(Resource):
    def get(self):
        self._add()
        return {'status': 'ok'}

    def delete(self):
        req = json.loads(request.data)
        with MSSQLDB() as db:
            # db.callproc()
            pass

    def post(self):
        req = json.loads(request.data)
        parse_api_req(req)

        return {}

    def _add(self):
        # TODO функция добавления мест в базу данных
        pass

    def _json(self, db_request) -> json:
        # TODO сделать запрос из БД, чтобы получить цены для мест посадки
        data = self._transfer()  # преобразование к нормальному виду
        return json.jsonify(data)

    def _transfer(self) -> json:
        # TODO написать функцию, которая преобразует данные для отправки
        return json
