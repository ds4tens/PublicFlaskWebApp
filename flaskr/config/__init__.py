from flaskr.parsetools import translator

DATABASE_CONF = translator('flaskr/config_files/database_conf.json')

DATABASE_PROCEDURES = list(translator('flaskr/config_files/db_procedures.json').values())
