from application import db
from sqlalchemy.sql import text
from application.auth.models import User


class HorseRiderLesson(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'),nullable=False)
    horse_id = db.Column(db.Integer, db.ForeignKey('horse.id'),nullable=True) 

    def __init__(self, account_id, lesson_id):
        self.account_id = account_id
        self.lesson_id = lesson_id
    
    @staticmethod
    def lessons_of_rider(id):
        lessons = []
        for object in db.session.query(HorseRiderLesson).filter_by(account_id=id):
            lessons.append(object.lesson_id)
        return lessons

    @staticmethod
    def riders_of_lesson(id):
        riders = []
        for object in db.session.query(HorseRiderLesson).filter_by(lesson_id=id):
            riders.append(object.account_id)
        return riders
    
    @staticmethod
    def get_rider_in_lesson(lesson_id,account_id):
        riders = db.session.query(HorseRiderLesson).filter_by(lesson_id=lesson_id)
        for rider in riders:
            if rider.account_id == account_id:
                return rider    

    @staticmethod
    def horses_of_lesson(id):
        horses = {}
        for object in db.session.query(HorseRiderLesson).filter_by(lesson_id=id):
            horses[object.horse_id] = User.query.get(object.account_id).name
        return horses