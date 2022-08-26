from unittest import registerResult
from forms import RegistrationForm
from flask import Flask, render_template, session , redirect, url_for,flash


app = Flask(__name__)

app.config['SECRET_KEY'] = "SAIHahHohFHoih"

@app.route('/',methods=['GET', 'POST'])
def index():

    form = RegistrationForm()

    if form.validate_on_submit():

        session['full_name'] = form.full_name.data
        form.full_name.data = ""
        session['email'] = form.email.data
        form.email.data = ""
        session['terms'] = form.terms.data
        
        flash(f"{session['full_name']} with the email id {session['email']} successfully registered.")

        if session['terms']:
            return redirect(url_for('thankyou'))
        
    return render_template('index.html',form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
 