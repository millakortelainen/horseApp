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
from functools import wraps
from flask_login import current_user

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# load application content
from application import views

from application.horses import models
from application.horses import views

from application.auth import models
from application.auth import views 

from application.lessons import models
from application.lessons import views

from application.horses_riders_lessons import models


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