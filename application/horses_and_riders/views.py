from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.horses_and_riders.forms import HorsesForRidersForm
from application.horses.models import Horse
from application.auth.models import User
from application.lessons.models import Lesson
from application.horses_and_riders.models import HorsesAndRiders


@app.route("/horses-and-riders/<lesson_id>")
def show_lesson(lesson_id):
    lessons_riders = []
    selected_horses_and_riders = HorsesAndRiders.query.all()
    riders = User.query.all()
    riders_with_horses = []
    horses_with_riders = {}

    for i in selected_horses_and_riders:
        if i.lesson_id == int(lesson_id):
            riders_with_horses.append(i.rider_id)
            horses_with_riders[i.horse_id]=User.query.get(i.rider_id).name

    for rider in riders:
        for lesson in rider.lessons:
            if (int(lesson_id) == lesson.id) and (rider.id not in riders_with_horses):
                lessons_riders.append((rider.id, rider.name))

    form = HorsesForRidersForm(request.form)
    form.riders.choices = lessons_riders

    return render_template("horses-and-riders/show-lesson.html",
                           lesson=Lesson.query.get(lesson_id), all_horses=Horse.query.all(),
                           horses_with_riders=horses_with_riders, selected_horses_and_riders=selected_horses_and_riders,
                           all_riders=riders, form=form)


@app.route("/horses-and-riders/validate/<lesson_id>and<horse_id>", methods=['POST'])
def validate_choices(lesson_id, horse_id):
    form = HorsesForRidersForm(request.form)
    horse_and_rider = HorsesAndRiders(lesson_id, horse_id, form.riders.data)
    db.session().add(horse_and_rider)
    db.session().commit()
    return redirect(url_for("show_lesson", lesson_id=lesson_id))
