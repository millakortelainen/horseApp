from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    username = StringField("Username", [validators.InputRequired()])
    password = StringField("Password", [validators.InputRequired()])
  
    class Meta:
        csrf = False
