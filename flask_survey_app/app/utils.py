from flask_mail import Message
from flask_survey_app.app import mail


def send_email(survey_results):
    msg = Message("Filled survey",
                  sender="from@mailtrap.io",
                  recipients=["to@mailtrap.io"])

    msg.body = f"""
    The survey has been filled by:
    {survey_results}
    """

    mail.send(msg)
