from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db
from application.lessons.models import Lesson
from application.lessons.forms import LessonForm
from application.horses.models import Horse
from application.auth.models import User

@app.route("/lessons/manage", methods=["GET"])
@login_required
def manage_lessons():
    lessons_riders = {}
    riders = User.query.all()
    for rider in riders:
        for lesson in rider.lessons:
            if not lesson.id in lessons_riders:
                lessons_riders[lesson.id]=[]
            lessons_riders[lesson.id].append([rider.id,rider.name])
    return render_template("lessons/manage-lessons.html", lessons=Lesson.query.all(), all_horses=Horse.query.all(), lessons_riders=lessons_riders)


@app.route("/lessons/new/")
@login_required
def lessons_form():
    return render_template("lessons/new.html", form=LessonForm())


@app.route("/lessons", methods=["GET"])
@login_required
def lessons_index():
    return render_template("lessons/list.html", lessons=Lesson.query.all(), all_horses=Horse.query.all())


@app.route("/lessons/", methods=["POST"])
@login_required
def lessons_create():
    form = LessonForm(request.form)
    lesson = Lesson(form.day.data, form.start_time.data, form.end_time.data,
               form.price.data, form.skill_level.data, form.type_of_lesson.data)

    db.session().add(lesson)
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

    lesson = Lesson.query.get(lesson_id)
    lesson.day = form.day.data
    lesson.start_time = form.start_time.data
    lesson.end_time = form.end_time.data
    lesson.price = form.price.data
    lesson.skill_level = form.skill_level.data
    lesson.type_of_lesson = form.type_of_lesson.data

    db.session().commit()

    return redirect(url_for("lessons_index"))


@app.route("/lessons/delete/<lesson_id>/", methods=["POST"])
@login_required
def delete_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)

    db.session.delete(lesson)

    db.session().commit()
    return render_template("lessons/list.html", lessons=Lesson.query.all(), all_horses=Horse.query.all())


@app.route("/lessons/sign-up/<lesson_id>/", methods=["POST"])
@login_required
def sign_up_for_lesson(lesson_id):
    user = current_user
    user.lessons.append(Lesson.query.get(lesson_id))
    db.session().add(user)
    db.session().commit()

    return redirect(url_for("lessons_index"))

@app.route("/lessons/save/<lesson_id>/", methods=["POST"])
@login_required
def save_lesson(lesson_id):
    return redirect(url_for("manage_lessons"))