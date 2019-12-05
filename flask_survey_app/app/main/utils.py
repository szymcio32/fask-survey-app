from flask import current_app
from flask_mail import Message
from threading import Thread

from flask_survey_app.app import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(survey_results):
    msg = Message("Filled survey",
                  sender="from@mailtrap.io",
                  recipients=["to@mailtrap.io"])

    msg.body = f"""
    The survey has been filled by:
    {survey_results}
    """

    mail_thread = Thread(target=send_async_email, args=(current_app._get_current_object(), msg))
    mail_thread.start()
