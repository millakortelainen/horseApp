from application import db
from application.models import Base
from sqlalchemy.sql import text

userlesson = db.Table('userlesson',
                      db.Column('user_id', db.Integer, db.ForeignKey(
                          'account.id'), primary_key=True),
                      db.Column('lesson_id', db.Integer, db.ForeignKey(
                          'lesson.id'), primary_key=True)
                      )


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    is_student = db.Column(db.Boolean, nullable=False)
    is_teacher = db.Column(db.Boolean, nullable=False)
    lessons = db.relationship(
        'Lesson', secondary=userlesson, backref='account')

    def __init__(self, name, username, password, is_teacher):
        self.name = name
        self.username = username
        self.password = password
        if is_teacher:
            self.is_student = False
            self.is_teacher = True
        else:
            self.is_student = True
            self.is_teacher = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN","USER"]

    @staticmethod
    def users_lessons():
    #     stmt = text("SELECT User.id, User.name FROM Lesson"
   #                 " LEFT JOIN Account ON Account.lesson_id = Lesson.id"
   #                 " GROUP BY Lesson.id")
   #     res = db.engine.execute(stmt)

   #     response = []
   #     for row in res:
   #         response.append(
   #             {"id": row[0], "day": row[1], "starts": row[2], "ends": row[3], "number_of_riders": row[4]})

        return 0
    
