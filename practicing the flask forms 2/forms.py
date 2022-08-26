from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional


class HotelForm(FlaskForm):

    name = StringField('Your Name',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    needed_service = SelectField('Needed Service', choices=[('1bhk','1bhk'),('2bhk','2bhk'),('3bhk','3bhk')])
    budget = SelectField('Budget',choices=[('less than $100','less than $100'), ('100$ to 500$d','$100 to $500'), ('$500 to $1000','$500 to $1000')])
    message  = StringField('Message',validators=[Optional()])
    submit = SubmitField('Submit')

