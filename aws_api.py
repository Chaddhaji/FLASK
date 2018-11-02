from flask import Flask
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = Flask('AWSAPI')

@app.route('/')
def index():
    return "HELLO WORLD"

if __name__ == "__main__":
    app.run()