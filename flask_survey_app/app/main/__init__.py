from flask import Blueprint

main_bp = Blueprint('main', __name__)

from flask_survey_app.app.main import routes