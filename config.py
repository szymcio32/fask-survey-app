class Config:
    SECRET_KEY = 'secret key'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:sim1990@localhost/survey_data"
    SQLALCHEMY_TRACK_MODIFICATIONS = False