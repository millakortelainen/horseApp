from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.lessons.models import Lesson
from application.lessons.forms import LessonForm


@app.route("/lessons/new/")
@login_required
def lessons_form():
    return render_template("lessons/new.html", form=LessonForm())


@app.route("/lessons", methods=["GET"])
@login_required
def lessons_index():
    return render_template("lessons/list.html", lessons=Lesson.query.all())


@app.route("/lessons/", methods=["POST"])
@login_required
def lessons_create():
    form = LessonForm(request.form)
    l = Lesson(form.day.data, form.start_time.data, form.end_time.data, form.price.data, form.skill_level.data, form.type_of_lesson.data)

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("lessons_index"))


@app.route("/lessons/<lesson_id>/", methods=["POST"])
@login_required
def edit_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    return render_template("lessons/edit-lesson.html", lesson=Lesson.query.get(lesson_id),
                           form=LessonForm(day=lesson.day, start_time=lesson.start_time, end_time=lesson.end_time,
                                           price=lesson.price, skill_level=lesson.skill_level, type_of_lesson=lesson.type_of_lesson))


@app.route("/lessons/update/<lesson_id>", methods=["POST"])
@login_required
def lessons_update(lesson_id):
    form = LessonForm(request.form)

    l = Lesson.query.get(lesson_id)
    l.day = form.day.data
    l.start_time = form.start_time.data
    l.end_time = form.end_time.data
    l.price = form.price.data
    l.skill_level = form.skill_level.data
    l.type_of_lesson = form.type_of_lesson.data

    db.session().commit()

    return redirect(url_for("lessons_index"))


@app.route("/lessons/delete/<lesson_id>/", methods=["POST"])
@login_required
def delete_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)

    db.session.delete(lesson)

    db.session().commit()
    return render_template("lessons/list.html", lessons=Lesson.query.all())
