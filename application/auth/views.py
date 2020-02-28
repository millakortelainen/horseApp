from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm, EditUserForm
from application.horses_riders_lessons.models import HorseRiderLesson
from application.lessons.models import Lesson

@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form=NewUserForm())


@app.route("/auth/", methods=["POST"])
def users_create():
    form = NewUserForm(request.form)
    if not form.validate():
        return render_template("auth/new.html", form=form)

    user = User(form.name.data, form.username.data, form.password.data, form.is_teacher.data)

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/auth/edit")
def user_edit():
    return render_template("auth/edit.html", form=EditUserForm())

@app.route("/auth/update/user", methods=["POST"])
def user_update():
    form = EditUserForm(request.form)
    current_user.skill_level = form.skill_level.data
    db.session().commit()
    return redirect(url_for("user_edit"))

@app.route("/auth/statistics")
def statistics():
    users_lessons = []
    lesson_ids = HorseRiderLesson.lessons_of_rider(current_user.id)
    for lesson_id in lesson_ids:
        users_lessons.append(Lesson.query.get(lesson_id))
    
    return render_template("auth/statistics.html", lessons=users_lessons, horse_data = User.horses_of_rider(current_user.id))
