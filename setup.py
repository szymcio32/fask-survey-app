from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name='survey-flask-app',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-mail",
        "flask-login",
        "flask-sqlalchemy",
        "flask-migrate",
        "python-dotenv",
        "psycopg2"
    ],
    author='szymcio32',
    description='Survey flask application',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/szymcio32/fask-survey-app',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'flask-survey-app = flask_survey_app.survey_app:run_app'
        ],
    }
)
