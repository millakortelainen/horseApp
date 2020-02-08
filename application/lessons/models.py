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

    riders = db.relationship("User", backref='lessons', lazy=True)

    def __init__(self, day, start_time, end_time, price, skill_level, type_of_lesson):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.skill_level = skill_level
        self.type_of_lesson = type_of_lesson

 #   @staticmethod
  #  def count_all_riders():
  #      stmt = text("SELECT Lesson.id, Lesson.day, Lesson.start_time, Lesson.end_time, COUNT(Account.id) FROM Lesson"
  #                  " LEFT JOIN Account ON Account.lesson_id = Lesson.id"
  #                  " GROUP BY Lesson.id")
  #      res = db.engine.execute(stmt)
        
 #       response = []
  #      for row in res:
  #          response.append({"id":row[0], "day":row[1], "starts":row[2], "ends":row[3], "number_of_riders":row[4]})
       
   #     return response