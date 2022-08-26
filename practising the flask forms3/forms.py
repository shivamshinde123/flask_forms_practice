from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, InputRequired, Length


class SignUpForm(FlaskForm):

    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators = [EqualTo('confirm',message='Password must match'), InputRequired(),Length(min=8,max=16)])
    confirm = PasswordField('Confirm Password',validators=[InputRequired()])
    login = SubmitField('Log In')