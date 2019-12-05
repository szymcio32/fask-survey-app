from flask_survey_app.config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'admin_panel.login'
login_manager.login_message_category = 'primary'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    from flask_survey_app.app import models
    from flask_survey_app.app.errors import errors_bp
    from flask_survey_app.app.admin_panel import admin_panel_bp
    from flask_survey_app.app.main import main_bp

    app.register_blueprint(errors_bp)
    app.register_blueprint(admin_panel_bp)
    app.register_blueprint(main_bp)

    return app
