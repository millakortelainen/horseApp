from application import app, db
from flask import redirect, render_template, request, url_for
from application.horses.models import Horse

@app.route("/horses/new/")
def horses_form():
    return render_template("horses/new.html")

@app.route("/horses", methods=["GET"])
def horses_index():
    return render_template("horses/list.html", horses = Horse.query.all())

@app.route("/horses/", methods=["POST"])
def horses_create():
    h = Horse(request.form.get("name"),request.form.get("gender"),request.form.get("breed"),request.form.get("skill_level"))
    
    db.session().add(h)
    db.session().commit()

    return redirect(url_for("horses_index"))

@app.route("/horses/<horse_id>/", methods=["POST"])
def edit_horse(horse_id):
    return render_template("horses/edit-horse.html", horse=Horse.query.get(horse_id))

@app.route("/horses/update/<horse_id>", methods=["POST"])
def horses_update(horse_id):
    h = Horse.query.get(horse_id)
    h.name = request.form.get("name")
    h.gender = request.form.get("gender")
    h.breed = request.form.get("breed")
    h.skill_level = request.form.get("skill_level")
    
    db.session().commit()

    return redirect(url_for("horses_index"))