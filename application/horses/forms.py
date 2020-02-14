from flask_wtf import FlaskForm
from wtforms import StringField, validators


class HorseForm(FlaskForm):
    name = StringField(
        "Name ", [validators.InputRequired(), validators.Length(max=140)])
    breed = StringField("Breed ", [validators.Length(max=140)])
    gender = StringField(
        "Gender", [validators.InputRequired(), validators.Length(max=10)])
    skill_level = StringField(
        "Skill level ", [validators.InputRequired(), validators.Length(max=50)])

    class Meta:
        csrf = False
