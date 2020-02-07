from flask_wtf import FlaskForm
from wtforms import StringField, DateField,DecimalField, validators

class LessonForm(FlaskForm):
    day = StringField("Date ", [validators.InputRequired()])
    start_time = StringField("Starts at ", [validators.InputRequired()])
    end_time = StringField("Ends at ", [validators.InputRequired()])
    price = StringField("Price ",[validators.InputRequired()])
    skill_level = StringField("Skill Level", [validators.InputRequired()])
    type_of_lesson = StringField("Type Of Lesson ", [validators.InputRequired()])
 
    class Meta:
        csrf = False
