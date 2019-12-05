from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash

from flask_survey_app.app import db
from flask_survey_app.app.models import SurveyResults
from flask_survey_app.app.main import main_bp
from flask_survey_app.app.main.utils import send_email


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if SurveyResults.is_email_in_database(email):
            flash(f"The user with {email} has already filled the survey", "danger")
            return redirect(url_for('index'))

        data = request.form.to_dict()
        single_results = SurveyResults(**data)
        db.session.add(single_results)
        db.session.commit()
        send_email(single_results)
        return render_template('success.html')
    return render_template('index.html')
