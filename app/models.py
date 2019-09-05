from app import db


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

