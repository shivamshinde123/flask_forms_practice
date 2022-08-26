from ast import In
from unittest.loader import VALID_MODULE_NAME
from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class SimpleForm(FlaskForm):

    breed = StringField('Breed',validators=[InputRequired()]);
    submit = SubmitField('Click Me.')