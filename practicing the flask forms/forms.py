from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, RadioField, SelectField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class PersonalDetails(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=8, max=16)])
    email = EmailField('Email', validators=[Email()])
    gender = RadioField('Gender', choices=[
                        ('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    contact = IntegerField('Contact', validators=[DataRequired()])
    degree = SelectField('Degreee', choices=[('X', '10th'), ('XII', '12th'), (
        'G', 'Graduate'), ('PG', 'Post-Graduate')], validators=[DataRequired()])
    hobby = SelectField(
        'Hobby', choices=[('sports', 'sports'), ('music', 'music')])
    address = TextAreaField('Address')
    submit = SubmitField('Submit')
