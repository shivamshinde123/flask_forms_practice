from xml.etree.ElementTree import fromstring
from flask import Flask, render_template,session, redirect, url_for
from forms import SignUpForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hjFJjJAKJkjflk'

@app.route('/',methods=['GET', 'POST'])
def index():

    form = SignUpForm()

    if form.validate_on_submit():

        session['username'] = form.username.data
        session['password'] = form.username.data

        return redirect(url_for('thankyou'))

    
    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
 