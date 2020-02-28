from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField, SelectField, BooleanField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired(),validators.Length(max=140)])
    username = StringField("Username", [validators.InputRequired(),validators.Length(max=140)])
    password = StringField("Password", [validators.InputRequired(),validators.Length(max=140)])
    is_teacher = BooleanField("This user is a teacher ")

    class Meta:
        csrf = False

class EditUserForm(FlaskForm):
    skill_level = SelectField(u'Skill Level', choices=[("easy", "Easy"), ("intermediate", "Intermediate"), ("advanced", "Advanced")])
    
    class Meta:
        csrf = False