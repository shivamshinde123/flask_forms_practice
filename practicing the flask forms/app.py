from statistics import fmean
from forms import PersonalDetails
from flask import Flask, render_template, session, redirect, url_for


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ISDHasdhfhhsAOIFH'



@app.route('/',methods=['GET', 'POST'])
def index():
    
    form = PersonalDetails()

    if form.validate_on_submit():

        session['name'] = form.name.data
        session['password'] = form.password.data
        session['email'] = form.email.data
        session['gender'] = form.gender.data
        session['contact'] = form.contact.data
        session['degree'] = form.degree.data
        session['hobby'] = form.hobby.data
        session['address'] = form.address.data

        return redirect(url_for('thankyou'))

    return render_template('index.html',form=form)

    
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
 