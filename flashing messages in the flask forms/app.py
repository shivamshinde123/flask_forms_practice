from flask import Flask, render_template,session, redirect , url_for, flash
from forms import SimpleForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SOFfiahOIFHfh'


@app.route('/',methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        
        session['breed'] = form.breed.data
        flash("Thank You! You have chosen {} breed of dog for adoption.")

        return redirect(url_for('thankyou'))

    return render_template('index.html',form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
 