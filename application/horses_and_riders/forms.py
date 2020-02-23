from flask_wtf import FlaskForm
from wtforms import SelectField, validators

class HorsesForRidersForm(FlaskForm):
    riders = SelectField(u'Riders', choices=[])

    class Meta:
        csrf = False
