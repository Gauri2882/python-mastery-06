""" Creating first flask route """

from flask import Flask

# create flask app
app = Flask(__name__)

# define a route
@app.route('/')
def hello():
    return "Hello, Gauri"

# run the app
if __name__ == "__main__":
    app.run(debug = True)