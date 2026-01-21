from flask import Flask, jsonify, redirect, render_template, url_for, request
from flask_cors import CORS
from markupsafe import escape
from dotenv import load_dotenv

import os


load_dotenv()


app = {
    "version": "0.0.0",
    "release_date": "01/01/0001"
}

user_dict = {
    "username": "john_doe123",
    "is_logged_in": False
}


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route('/')
def index():
    user = user_dict if user_dict["is_logged_in"] else None

    return render_template("base.html", user=user, app=app)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route("/register", methods=["GET", "POST"])
def register():

    return render_template('register.html', user=None, app=app)

@app.route("/login", methods=["GET", "POST"])
def login():

    return render_template('login.html', user=None, app=app)

@app.route("/support", methods=["GET", "POST"])
def support():

    return render_template('support.html', user=None, app=app)

@app.route("/about")
def about():
    dev_info = {
        "name": "mek0124",
        "repo": "https://github.com/mek0124",
        "experience": [
            { "language": "Python", "years": "9" },
            { "language": "Java Script", "years": "7" },
            { "language": "C#", "years": "< 1" },
            { ""}
        ]
    }

    return render_template('about.html', dev=dev_info, app=app)

if __name__ == '__main__':
    app.run(debug=True)
