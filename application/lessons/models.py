from application import db
from application.models import Base
from sqlalchemy.sql import text

class Lesson(Base):

    day = db.Column(db.String(30), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    skill_level = db.Column(db.String(144), nullable=True)
    type_of_lesson = db.Column(db.String(144), nullable=True)

    def __init__(self, day, start_time, end_time, price, skill_level, type_of_lesson):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.skill_level = skill_level
        self.type_of_lesson = type_of_lesson