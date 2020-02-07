from application import db
from application.models import Base
from sqlalchemy.sql import text

class Horse(Base):
  
    name = db.Column(db.String(144), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    breed = db.Column(db.String(144), nullable=True)
    skill_level = db.Column(db.String(50), nullable=False)

    def __init__(self, name, gender, breed, skill_level):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.skill_level = skill_level

