from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin

from flask_survey_app.app import db
from flask_survey_app.app import login_manager


@login_manager.user_loader
def load_user(id):
    return AdminUsers.query.get(int(id))


class SurveyResults(db.Model):
    __tablename__ = "survey_results"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    gender = db.Column(db.String(64))
    age = db.Column(db.String(20))
    recommendation = db.Column(db.String(20))
    like = db.Column(db.Text(300))
    dislike = db.Column(db.Text(300))
    organization = db.Column(db.String(20))
    helpful = db.Column(db.String(20))

    def __repr__(self):
        return f'Name: {self.name} Email: {self.email}'

    @staticmethod
    def is_email_in_database(email):
        return True if SurveyResults.query.filter_by(email=email).first() else False


class AdminUsers(db.Model, UserMixin):
    __tablename__ = "admin_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'Admin user: {self.username}'

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def is_password_correct(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_admin_user(cls, username):
        return AdminUsers.query.filter_by(username=username).first()

    @staticmethod
    def is_username_in_database(username):
        return True if AdminUsers.query.filter_by(username=username).first() else False
