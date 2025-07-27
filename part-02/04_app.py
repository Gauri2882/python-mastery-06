""" Dynamic Templates with Jinja2 """

from flask import Flask, render_template

app =  Flask(__name__)

# static route
@app.route('/')
def home():
    return render_template('index.html', title = "Welcome to Gauri's Blog")

if __name__ == "__main__":
    app.run(debug= True)