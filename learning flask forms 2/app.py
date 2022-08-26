from math import frexp
from statistics import fmean
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, BooleanField, RadioField, SelectField,  TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

app.config['SECRET_KEY'] = "ASOIIOKJSDFkf"


class InfoForm(FlaskForm):

    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Habe you been neutered?',
                            validators=[DataRequired()])
    mood = RadioField('Please choose your mood.', choices=[
                      ('hpy', 'Happy'), ('exd', 'excited')])
    food_choice = SelectField('Pick your favorite food:', choices=[
                              ('bf', 'beef'), ('chkn', 'chicken'), ('fh', 'fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():

        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
