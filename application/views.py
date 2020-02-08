from flask import render_template
from application import app
from application.lessons.models import Lesson

@app.route("/")
def index():
    return render_template("index.html", all_riders=Lesson.count_all_riders())
