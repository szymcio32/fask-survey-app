import os
from dotenv import load_dotenv


base_dir = os.path.abspath(os.path.dirname(__file__))
env_file = os.path.join(base_dir, ".env")
if os.path.isfile(env_file):
    load_dotenv(env_file)


class Config:
    SECRET_KEY = 'secret key'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.mailtrap.io"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
