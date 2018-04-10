from datetime import datetime
from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(error):
    return "Internal Server Error:  you bwoke it UwU",500

@app.route("/")
def root():
    return redirect(url_for("index"))

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def contact():
    return "contact me placeholder"

@app.route("/derby")
def derby():
    return "placeholder for derby info page, a hobby"

if __name__ == "__main__":
    app.run()
