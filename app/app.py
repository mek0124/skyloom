from flask import Flask, jsonify, redirect, render_template, url_for, request
from flask_cors import CORS
from markupsafe import escape
from dotenv import load_dotenv
from datetime import datetime

import requests
import os


load_dotenv()


app = {
    "version": "0.0.0",
    "release_date": "01/01/0001"
}

user_dict = {
    "username": "john_doe123",
    "icon": "icon.jpeg",
    "is_logged_in": True
}


app = Flask(__name__)
CORS(app)

app.config["WEATHER_API_KEY"] = os.getenv("WEATHER_API_KEY")
app.config["WEATHER_API_URL_BASE"] = os.getenv("WEATHER_API_URL_BASE")
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
            { "language": "Bash", "years": "3" },
        ]
    }

    return render_template('about.html', dev=dev_info, app=app)

@app.route("/dashboard")
def dashboard():
    # only hard coded address to try and get working response
    address = "225 Wicker Rd. Cowarts, AL, USA 36321"
    api_key = app.config["WEATHER_API_KEY"]

    request_data = {
        "key": api_key,
        "q": address,
        "hour": datetime.now().hour(),
        "alerts": "yes"
    }

    current_weather = requests.get('http://127.0.0.1/daily_forecast', request_data)
    return render_template('dashboard.html', user=user_dict, app=app)

@app.route("/daily_forecast")
def daily_forecast():
    try:
        response = requests.get(
            app.config["WEATHER_API_URL_BASE"] + "/current.json",
            )

        print(response)
        return render_template('dashboard', user=user_dict, app=app)
    
    except Exception as e:
        print(f"Unknown Exception Getting Current Weather: {e}")
        return render_template('dashboard', user=user_dict, app=app)

@app.route("/weekly_forecast")
def weekly_forecast():
    pass

@app.route("/monthly_forecast")
def monthly_forecast():
    pass

@app.route("/yearly_forecast")
def yearly_forecast():
    pass

@app.route("/profile")
def profile():
    pass

@app.route("/settings")
def settings():
    pass

if __name__ == '__main__':
    app.run(debug=True)
