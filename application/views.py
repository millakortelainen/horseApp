from flask import render_template
from application import app
from application.horses.models import Horse

@app.route("/")
def index():
    return render_template("index.html")
