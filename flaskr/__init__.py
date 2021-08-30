import os

from flask import Flask


def create_app(test_config=None, *args):
    # создание и настройка приложения
    app = Flask(__name__, instance_relative_config=True, *args)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    if test_config is None:
        # запуск стандартных настроек, если не в режиме тестов
        app.config.from_pyfile('config.py', silent=True)
    else:
        # загрузка с настройками для тестов
        app.config.from_mapping(test_config)

    # проверка есть ли рабочая папка
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import webhook
    app.register_blueprint(webhook.bp)  # регистрация БП (для обработки вебхуков) внутри приложения

    from flaskr.api import blu_api
    app.register_blueprint(blu_api)  # регистрация БП (для работы с api) внутри приложения

    return app
