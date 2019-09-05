from flask import render_template
from flask import request
from flask import flash

from app import app
from app import db
from app.models import SurveyResults


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        email = request.form['email']
        if SurveyResults.is_email_in_database(email):
            # @TODO: return error page
            error = f"The user with {email} has already filled the survey"
            return render_template('index.html', error=error), 409

        data = request.form.to_dict()
        single_results = SurveyResults(**data)
        db.session.add(single_results)
        db.session.commit()
        # @TODO: success page
    return render_template('index.html')