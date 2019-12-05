from flask import Blueprint

errors_bp = Blueprint('errors', __name__)

from flask_survey_app.app.errors import routes