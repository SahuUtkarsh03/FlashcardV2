import os
from flask import Flask
from flask_restful import Api
from application.config import LocalDevelopmentConfig
from application.data.database import db
from flask_cors import CORS
import application.jobs.workers as workers
from flask_caching import Cache

app = None
api = None
celery = None
cache = None

def create_app():
    app= Flask(__name__,static_folder="static",template_folder="templates")

    if os.getenv('ENV',"development") == "production":
        raise Exception("No production config setup")
    else:
        print("Starting local development")
        app.config.from_object(LocalDevelopmentConfig)
    app.app_context().push()

    db.init_app(app)
    app.app_context().push()
    
    api=Api(app)
    app.app_context().push()

    CORS(app)
    app.app_context().push()

    celery=workers.celery
    celery.conf.update(
        broker_url = app.config["CELERY_BROKER_URL"],
        result_backend = app.config["CELERY_RESULT_BACKEND"]
    )   
    celery.Task = workers.ContextTask
    app.app_context().push()

    cache=Cache(app)
    app.app_context().push()

    return app, api, celery, cache

app,api,celery,cache = create_app()

#adding all RESTful controllers
from application.controller.api.cardapi import CardApi
from application.controller.api.deckapi import DeckApi
from application.controller.api.userapi import UserApi

# mapping Apiclass to respective paths
api.add_resource(UserApi,"/user/<string:username>", "/user")
api.add_resource(DeckApi,"/deck/<int:deckid>","/deck")
api.add_resource(CardApi,"/card/<int:cardid>","/card")

from application.controller.controllers import *

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
