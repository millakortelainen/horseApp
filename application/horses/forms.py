from flask_wtf import FlaskForm
from wtforms import SelectField,StringField, validators


class HorseForm(FlaskForm):
    name = StringField(
        "Name ", [validators.InputRequired(), validators.Length(max=140)])
    breed = StringField("Breed ", [validators.Length(max=140)])
    gender = StringField(
        "Gender", [validators.InputRequired(), validators.Length(max=10)])
    skill_level = SelectField(u'Skill Level', choices=[("easy", "Easy"), ("intermediate", "Intermediate"), ("advanced", "Advanced")])
    
    class Meta:
        csrf = False
