""" Passing data between routes and Templates """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [
        {"id": 1, "title": "First Post", "content": "This is my first blog post"},
        {"id": 2, "title": "Second Post", "content": "This is my second blog post"}
    ]
    return render_template('index1.html', posts = posts)


if __name__ == "__main__":
    app.run(debug= True)