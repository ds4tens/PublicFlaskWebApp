from flaskr.api.v1.resource.method import SeatingChart
from flaskr.api import api


def api_get():
    api.add_resource(SeatingChart, '/')
