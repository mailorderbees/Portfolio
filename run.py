from datetime import datetime
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(error):
    return "Internal Server Error:  you bwoke it UwU",500
