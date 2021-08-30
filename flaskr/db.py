import pymssql
from flaskr.config import DATABASE_CONF


class MSSQLDB():

    def __init__(self):
        self._conect()
        self.cursor = self._cnx.cursor()

    def __enter__(self):
        self._conect()
        self.cursor = self._cnx.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def callproc(self, proc_name: str, *args: list):
        """Обращение к определнной процедуре БД с передачей аргументов"""
        self.cursor.callproc(proc_name, args)
        self._cnx.commit()

    def _conect(self, conf=DATABASE_CONF):
        """Подключение к БД"""
        self._cnx = pymssql.connect(
            **conf
        )
