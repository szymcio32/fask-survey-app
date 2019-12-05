# Flask survey application

Event feedback application built with Flask. A user can fill out the survey and send the answer to the admin.
After filling the form admin will be automatically notify via email that somebody has sent a filled form.

There is also a admin dashboard, which contain all survey results sent by users.

The purpose of the project was to learn Flask Framework

## Setup

**METHOD 1**

- Create a virtual environment
```buildoutcfg
python -m venv venv
```
- Add a postgres database uri to environment variables
```buildoutcfg
set DATABASE_URI=postgresql://<username>:<password>@<host>
```
- Add username and password for your mailtrap account
```buildoutcfg
set MAIL_USERNAME=<username>
set MAIL_PASSWORD=<password>
```
- In survey-flask-app directory run command:
```buildoutcfg
python setup.py install
```
- After that run command
```buildoutcfg
flask-survey-app 
```

**METHOD 2**

- Create a virtual environment
```buildoutcfg
python -m venv venv
```
- Add a postgres database uri to environment variables
```buildoutcfg
set DATABASE_URI=postgresql://<username>:<password>@<host>
```
- Add username and password for your mailtrap account
```buildoutcfg
set MAIL_USERNAME=<username>
set MAIL_PASSWORD=<password>
```
- Install packages from requirements.txt
```buildoutcfg
pip install -r requirements.txt
```
- After that run command
```buildoutcfg
python flask_survey_app\survey_app.py
```

## Example of app
Home page

![flask-home-1](https://user-images.githubusercontent.com/32844693/67413256-1ae1a700-f5c1-11e9-80d5-0612f583c415.PNG)

![flask-home-2](https://user-images.githubusercontent.com/32844693/67413251-1a491080-f5c1-11e9-9552-29037e622f84.PNG)

After filling out form

![flask-success](https://user-images.githubusercontent.com/32844693/67413253-1a491080-f5c1-11e9-8d63-90ad02c36888.PNG)

Admin panel login page

![flask-admin-login](https://user-images.githubusercontent.com/32844693/67413252-1a491080-f5c1-11e9-9b06-2b65919867ed.PNG)

Admin dashboard

![flask-admin-panel](https://user-images.githubusercontent.com/32844693/67413254-1ae1a700-f5c1-11e9-8b13-3558f11aa449.PNG)


## Technologies

- Python 3.7.0
- Flask 1.1.1
- PostgreSQL
- HTML / CSS / JS
- Bootstrap 4.3.1
- mailtrap.io