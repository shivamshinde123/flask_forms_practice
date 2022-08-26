from flask import Flask, render_template, session, redirect, url_for
from forms import HotelForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'LDSsdhiLAoihiofh'


@app.route('/',methods=['GET', 'POST'])
def index():
    
    form = HotelForm()

    if form.validate_on_submit():

        session['name'] = form.name.data
        session['email'] = form.email.data
        session['needed_service'] = form.needed_service.data
        session['budget'] = form.budget.data
        session['message'] = form.message.data

        return redirect(url_for('thankyou'))


    return render_template('index.html',form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
 