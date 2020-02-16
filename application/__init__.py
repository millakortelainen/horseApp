from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import sys
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///horses.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# kirjautuminen
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required

# load application content
from application import views

from application.horses import models
from application.horses import views

from application.auth import models
from application.auth import views 

from application.lessons import models
from application.lessons import views

from application.horses_and_riders import models


# login functionality, part 2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database creation
try: 
    db.create_all()
except:
    print(sys.exc_info())
    pass