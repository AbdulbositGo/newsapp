from flask import render_template

from config import app

@app.errorhandler(404)
def error_handler(e):
    return render_template("client/error.html")