from flask_survey_app.config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'primary'

mail = Mail(app)

from flask_survey_app.app import routes
from flask_survey_app.app import models
from flask_survey_app.app import errors
