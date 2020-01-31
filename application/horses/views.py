from application import app, db
from flask import redirect, render_template, request, url_for
from application.horses.models import Horse
from application.horses.forms import HorseForm

@app.route("/horses/new/")
def horses_form():
    return render_template("horses/new.html", form=HorseForm())


@app.route("/horses", methods=["GET"])
def horses_index():
    return render_template("horses/list.html", horses=Horse.query.all())


@app.route("/horses/", methods=["POST"])
def horses_create():
    form = HorseForm(request.form)

    if not form.validate():
        return render_template("horses/new.html", form=form)

    h = Horse(form.name.data, form.gender.data,
              form.breed.data, form.skill_level.data)

    db.session().add(h)
    db.session().commit()

    return redirect(url_for("horses_index"))


@app.route("/horses/<horse_id>/", methods=["POST"])
def edit_horse(horse_id):
    horse = Horse.query.get(horse_id)
    return render_template("horses/edit-horse.html", horse=Horse.query.get(horse_id),
                           form=HorseForm(name=horse.name,
                                              breed=horse.breed,
                                              gender=horse.gender,
                                              skill_level=horse.skill_level))


@app.route("/horses/update/<horse_id>", methods=["POST"])
def horses_update(horse_id):
    form = HorseForm(request.form)

    if not form.validate():
        return render_template("horses/edit-horse.html", form=form)

    h = Horse.query.get(horse_id)
    h.name = form.name.data
    h.gender = form.gender.data
    h.breed = form.breed.data
    h.skill_level = form.skill_level.data

    db.session().commit()

    return redirect(url_for("horses_index"))

@app.route("/horses/delete/<horse_id>/", methods=["POST"])
def delete_horse(horse_id):
    horse = Horse.query.get(horse_id)

    db.session.delete(horse)

    db.session().commit()
    return render_template("horses/list.html", horses=Horse.query.all())
