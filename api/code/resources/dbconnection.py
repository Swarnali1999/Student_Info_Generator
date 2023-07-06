from flask import Flask
import resources.config as config
from flask_sqlalchemy import SQLAlchemy

config_object = config.Config()

class GetConfig:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{0}:{1}@{2}:5432/{3}".format(config_object.DB_USER, config_object.DB_PASS, config_object.DB_HOST, config_object.DB_NAME)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
  
    db = SQLAlchemy(app, session_options={'autocommit': True})