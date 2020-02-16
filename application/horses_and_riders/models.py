from application import db
from application.models import Base
from sqlalchemy.sql import text


class HorsesAndRiders(Base):

    lesson_id = db.Column(db.Integer, nullable=False)
    horse_id = db.Column(db.Integer, nullable=False)
    rider_id = db.Column(db.Integer, nullable=False)

    def __init__(self, lesson_id, horse_id, rider_id):
        self.lesson_id = lesson_id
        self.horse_id = horse_id
        self.rider_id = rider_id
