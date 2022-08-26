from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class RegistrationForm(FlaskForm):

    full_name = StringField('Full Name',validators=[InputRequired()])
    email = EmailField('Email',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired(), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Confirm Password')
    terms = BooleanField()
    submit = SubmitField('Register')


