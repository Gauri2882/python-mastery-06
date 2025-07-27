""" Project: Contact Form App """

from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# contact form class
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    message = TextAreaField('Message', validators= [DataRequired()])
    submit = SubmitField('Submit')

# route for contact form
@app.route('/', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Thank you, {form.name.data}! Your message has been sent.", "Success")
        return redirect(url_for('success'))
    return render_template('contact.html', form = form)

# success page
@app.route('/success')
def success():
    return render_template('success.html')

# run the app
if __name__ == "__main__":
    app.run(debug= True)