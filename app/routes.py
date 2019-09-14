from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from app import app
from app import db
from app.models import SurveyResults
from app.models import AdminUsers


# TODO: admin page
# TODO: change admin password
# TODO: email sending
# TODO: .env variables
# TODO: setup.py
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if SurveyResults.is_email_in_database(email):
            flash(f"The user with {email} has already filled the survey", "danger")
            return render_template('index.html'), 409

        data = request.form.to_dict()
        single_results = SurveyResults(**data)
        db.session.add(single_results)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_panel'))
    if request.method == 'POST':
        username = request.form['login-username']
        password = request.form['login-password']
        admin_user = AdminUsers.get_admin_user(username)
        if admin_user is None or not admin_user.check_password_hash(password):
            flash(f"Invalid username or password", "danger")
            return redirect(url_for('login'))
        login_user(admin_user)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('admin_panel'))
    return render_template('login.html')


@app.route('/add-admin', methods=['GET', 'POST'])
@login_required
def add_admin():
    if request.method == 'POST':
        username = request.form['add-admin-username']
        password = request.form['add-admin-password']
        confirm_password = request.form['add-admin-confirm-password']
        if AdminUsers.is_username_in_database(username):
            flash(f"Admin user '{username}' already exist", "danger")
            return redirect(url_for('add_admin'))
        if password != confirm_password:
            flash(f"Password does not match", "danger")
            return redirect(url_for('add_admin'))
        admin_user = AdminUsers(username=username)
        admin_user.set_password_hash(password)
        db.session.add(admin_user)
        db.session.commit()
        flash(f"The user '{username}' has been successfully created", "primary")
        return redirect(url_for('add_admin'))
    return render_template('add_admin_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/admin-panel')
@login_required
def admin_panel():
    return render_template('admin_panel.html')