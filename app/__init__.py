from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

from  app.config import Config
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from app import models, flask_api
api.add_resource(flask_api.FileOperation, '/files/<filename>')
api.add_resource(flask_api.Auth, '/auth')

