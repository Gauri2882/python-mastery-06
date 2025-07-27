""" Understanding flask templates """

from flask import Flask, render_template

# create flask app
app = Flask(__name__)

# define a route
@app.route('/')
def hello():
    return render_template('index.html', name = "Gauri")

# run the app
if __name__ == "__main__":
    app.run(debug = True)