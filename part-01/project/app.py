""" Project: Hello Flask App """

from flask import Flask, render_template

# create flask app
app = Flask(__name__)

# define a route
@app.route('/')
def home():
    return render_template('index.html')

# greeting route
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name = name)

# run the app
if __name__ == "__main__":
    app.run(debug = True)