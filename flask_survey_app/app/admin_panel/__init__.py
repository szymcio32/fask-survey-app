from flask import Blueprint

admin_panel_bp = Blueprint('admin_panel', __name__)

from flask_survey_app.app.admin_panel import routes