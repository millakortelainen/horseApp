from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, DecimalField, validators


class LessonForm(FlaskForm):
    day = StringField(
        "Date ", [validators.InputRequired(), validators.Length(max=30)])
    start_time = StringField(
        "Starts at ", [validators.InputRequired(), validators.Length(max=10)])
    end_time = StringField(
        "Ends at ", [validators.InputRequired(), validators.Length(max=10)])
    price = StringField(
        "Price ", [validators.InputRequired(), validators.Length(max=140)])
    skill_level = SelectField(u'Skill Level', choices=[("easy", "Easy"), ("intermediate", "Intermediate"), ("advanced", "Advanced")])
    type_of_lesson = StringField(
        "Type Of Lesson ", [validators.Length(max=140)])

    class Meta:
        csrf = False