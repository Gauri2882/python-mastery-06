""" Setting up Flask REST API """

from flask import Flask, jsonify

app = Flask(__name__)

# root endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Mini Weather API!"})

if __name__ == "__main__":
    app.run(debug= True)