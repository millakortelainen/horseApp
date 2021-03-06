from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.lessons.models import Lesson
from application.lessons.forms import LessonForm, EditLessonForm
from application.horses.models import Horse
from application.auth.models import User
from application.horses_riders_lessons.models import HorseRiderLesson
from application.horses_riders_lessons.forms import HorsesForRidersForm


@app.route("/lessons/manage", methods=["GET"])
@login_required(role="ADMIN")
def manage_lessons():
    return render_template("lessons/manage-lessons.html", lessons=Lesson.query.all())


@app.route("/lessons/new/")
@login_required(role="ADMIN")
def lessons_form():
    return render_template("lessons/new.html", form=LessonForm())


@app.route("/lessons", methods=["GET"])
@login_required
def lessons_index():
    return render_template("lessons/list.html", lessons=Lesson.get_lessons(current_user.skill_level), lessons_of_rider=HorseRiderLesson.lessons_of_rider(current_user.id))


@app.route("/lessons/", methods=["POST"])
@login_required(role="ADMIN")
def lessons_create():
    form = LessonForm(request.form)
    lesson = Lesson(form.day.data, form.start_time.data, form.end_time.data,
                    form.price.data, form.skill_level.data, form.type_of_lesson.data)

    db.session().add(lesson)
    db.session().commit()
    return redirect(url_for("lessons_index"))


@app.route("/lessons/<lesson_id>/", methods=["POST"])
@login_required(role="ADMIN")
def edit_lesson(lesson_id):
    lesson=Lesson.query.get(lesson_id)

    return render_template("lessons/edit-lesson.html", lesson=Lesson.query.get(lesson_id),
                           form=EditLessonForm(day=lesson.day, start_time = lesson.start_time, end_time =lesson.end_time, price = int(lesson.price), skill_level = lesson.skill_level, type_of_lesson=lesson.type_of_lesson))


@app.route("/lessons/set-horses/<lesson_id>/", methods=["POST"])
@login_required(role="ADMIN")
def set_horses(lesson_id):
    lesson=Lesson.query.get(lesson_id)
    lessons_riders = []
    riders = db.session.query(HorseRiderLesson).filter_by(lesson_id=lesson_id)
    for rider in riders:
        if rider.horse_id is None:
            lessons_riders.append(
                (rider.account_id, User.query.get(rider.account_id).name))

    form = HorsesForRidersForm(request.form)
    form.riders.choices = lessons_riders

    return render_template("lessons/horses-for-riders-at-lesson.html", lesson=Lesson.query.get(lesson_id), horses=Horse.get_horses(lesson.skill_level),
                           form=form, horses_at_lesson=HorseRiderLesson.horses_of_lesson(lesson_id))


@app.route("/lessons/set-horse/<lesson_id>and<horse_id>/", methods=["POST"])
@login_required(role="ADMIN")
def set_horse(lesson_id, horse_id):
    form = HorsesForRidersForm(request.form)
    if form.riders.data == "None":
        return redirect(url_for("index"))

    rider = HorseRiderLesson.get_rider_in_lesson(
        int(lesson_id), int(form.riders.data))
    rider.horse_id = horse_id
    db.session().commit()
    return redirect(url_for("manage_lessons"))


@app.route("/lessons/update/<lesson_id>", methods=["POST"])
@login_required(role="ADMIN")
def lessons_update(lesson_id):
    form = LessonForm(request.form)

    lesson = Lesson.query.get(lesson_id)
    lesson.day = form.day.data
    lesson.start_time = form.start_time.data
    lesson.end_time = form.end_time.data
    lesson.price = form.price.data
    lesson.type_of_lesson = form.type_of_lesson.data

    db.session().commit()

    return redirect(url_for("manage_lessons"))


@app.route("/lessons/delete/<lesson_id>/", methods=["POST"])
@login_required(role="ADMIN")
def delete_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    all_references = HorseRiderLesson.query.all()

    for ref in all_references:
        if(ref.lesson_id == int(lesson_id)):
            db.session.delete(ref)

    db.session.delete(lesson)

    db.session().commit()
    return redirect(url_for("manage_lessons"))


@app.route("/lessons/sign-up/<lesson_id>/", methods=["POST"])
@login_required
def sign_up_for_lesson(lesson_id):
    lessons_of_rider = HorseRiderLesson.lessons_of_rider(current_user.id)
    if(int(lesson_id) not in lessons_of_rider):
        rider_to_lesson = HorseRiderLesson(current_user.id, lesson_id)
        db.session().add(rider_to_lesson)
        db.session().commit()

    return redirect(url_for("lessons_index"))


@app.route("/lessons/cancel/<lesson_id>/", methods=["POST"])
@login_required
def cancel_lesson(lesson_id):
    all_references = HorseRiderLesson.query.all()

    for ref in all_references:
        if(ref.lesson_id == int(lesson_id)):
            db.session.delete(ref)

    db.session().commit()
    return redirect(url_for("lessons_index"))
