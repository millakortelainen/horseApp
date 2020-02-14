from application import db
from application.models import Base
from sqlalchemy.sql import text

horselesson = db.Table('horselesson',
    db.Column('horse_id', db.Integer, db.ForeignKey('horse.id'), primary_key=True),
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True)
)

class Horse(Base):

    name = db.Column(db.String(144), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    breed = db.Column(db.String(144), nullable=True)
    skill_level = db.Column(db.String(50), nullable=False)
    lessons = db.relationship('Lesson', secondary=horselesson, backref='horses')

    def __init__(self, name, gender, breed, skill_level):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.skill_level = skill_level
