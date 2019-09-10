from flask import render_template
from flask import request

from app import app
from app import db
from app.models import SurveyResults
from app.models import AdminUsers

# TODO: login page
# TODO: add admin user page
# TODO: change admin password
# TODO: admin user database + password validation
# TODO: admin page
# TODO: email sending
# TODO: .env variables
# TODO: setup.py
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if SurveyResults.is_email_in_database(email):
            error = f"The user with {email} has already filled the survey"
            return render_template('index.html', error=error), 409

        data = request.form.to_dict()
        single_results = SurveyResults(**data)
        db.session.add(single_results)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['login-username']
        password = request.form['login-password']
        if not AdminUsers.is_username_in_database(username):
            error = f"Admin user '{username}' not found"
            return render_template('login.html', error=error), 404

    return render_template('login.html')


@app.route('/add-admin', methods=['GET', 'POST'])
def add_admin():
    return render_template('add_admin_user.html')