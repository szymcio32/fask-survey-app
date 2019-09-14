from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin

from app import db
from app import login_manager


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
        return f'SurveyResults {self.name} {self.email}'

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

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_admin_user(cls, username):
        return AdminUsers.query.filter_by(username=username).first()

    @staticmethod
    def is_username_in_database(username):
        return True if AdminUsers.query.filter_by(username=username).first() else False
