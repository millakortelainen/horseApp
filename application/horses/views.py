from application import app, db, login_required
from flask import redirect, render_template, request, url_for

from application.horses.models import Horse
from application.horses.forms import HorseForm
from application.horses_riders_lessons.models import HorseRiderLesson


@app.route("/horses/new/")
@login_required(role="ADMIN")
def horses_form():
    return render_template("horses/new.html", form=HorseForm())


@app.route("/horses", methods=["GET"])
@login_required(role="ADMIN")
def horses_index():
    return render_template("horses/list.html", horses=Horse.query.all())


@app.route("/horses/", methods=["POST"])
@login_required(role="ADMIN")
def horses_create():
    form = HorseForm(request.form)

    if not form.validate():
        return render_template("horses/new.html", form=form)

    horse = Horse(form.name.data, form.gender.data,
                  form.breed.data, form.skill_level.data)

    db.session().add(horse)
    db.session().commit()

    return redirect(url_for("horses_index"))


@app.route("/horses/<horse_id>/", methods=["POST"])
@login_required(role="ADMIN")
def edit_horse(horse_id):
    horse = Horse.query.get(horse_id)
    return render_template("horses/edit-horse.html", horse=Horse.query.get(horse_id),
                           form=HorseForm(name=horse.name,
                                          breed=horse.breed,
                                          gender=horse.gender,
                                          skill_level=horse.skill_level))


@app.route("/horses/update/<horse_id>", methods=["POST"])
@login_required(role="ADMIN")
def horses_update(horse_id):
    form = HorseForm(request.form)

    if not form.validate():
        return render_template("horses/edit-horse.html", form=form)

    horse = Horse.query.get(horse_id)
    horse.name = form.name.data
    horse.gender = form.gender.data
    horse.breed = form.breed.data
    horse.skill_level = form.skill_level.data

    db.session().commit()

    return redirect(url_for("horses_index"))


@app.route("/horses/delete/<horse_id>/", methods=["POST"])
@login_required(role="ADMIN")
def delete_horse(horse_id):
    horse = Horse.query.get(horse_id)
    all_horses_in_lessons = HorseRiderLesson.query.all()

    for ref in all_horses_in_lessons:
        if(ref.horse_id == int(horse_id)):
            ref.horse_id = None

    db.session.delete(horse)

    db.session().commit()
    return redirect(url_for("horses_index"))
