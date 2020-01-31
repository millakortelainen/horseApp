from flask_wtf import FlaskForm
from wtforms import StringField, validators

class HorseForm(FlaskForm):
    name = StringField("Name ", [validators.InputRequired()])
    breed = StringField("Breed ")
    gender = StringField("Gender", [validators.InputRequired()])
    skill_level = StringField("Skill level ", [validators.InputRequired()])
 
    class Meta:
        csrf = False
