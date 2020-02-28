from application import db
from application.models import Base
from sqlalchemy.sql import text

class Horse(Base):

    name = db.Column(db.String(144), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    breed = db.Column(db.String(144), nullable=True)
    skill_level = db.Column(db.String(50), nullable=True)
    lessons = db.relationship("HorseRiderLesson", backref='horse', lazy=True)

    def __init__(self, name, gender, breed, skill_level):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.skill_level = skill_level

    @staticmethod
    def get_horses(skill_level):
        horses = []
        if(skill_level == "easy"):
            horses = Horse.query.all()
        elif(skill_level == "intermediate"):
            for horse in db.session.query(Horse).filter_by(skill_level=skill_level):
                horses.append(horse)
            for horse in db.session.query(Horse).filter_by(skill_level="advanced"):
                horses.append(horse)
        else:
            for horse in db.session.query(Horse).filter_by(skill_level=skill_level):
                horses.append(horse)
        
        return horses