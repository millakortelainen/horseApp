from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    is_student = db.Column(db.Boolean, nullable=False)
    is_teacher = db.Column(db.Boolean, nullable=False)
    skill_level = db.Column(db.String(50), nullable=True)
    lessons = db.relationship("HorseRiderLesson", backref='account', lazy=True)

    def __init__(self, name, username, password, is_teacher):
        self.name = name
        self.username = username
        self.password = password
        if is_teacher:
            self.is_student = False
            self.is_teacher = True
            self.skill_level = "advanced"
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
        if(self.is_student):
            return ["USER"]
        else:
            return ["ADMIN"]

    @staticmethod
    def horses_of_rider(user_id):

        stmt = text("SELECT Horse.id, Horse.name, Horse.breed, Horse.gender, COUNT(Account.id) FROM Horse"
                    " LEFT OUTER JOIN horse_rider_lesson ON Horse.id = horse_rider_lesson.horse_id"
                    " LEFT OUTER JOIN account ON horse_rider_lesson.account_id = account.id"
                    " WHERE Account.id = :a"
                    " GROUP BY Horse.id")
        res = db.engine.execute(stmt, a=user_id)

        response = []
        for row in res:
            response.append(
                {"id": row[0], "name": row[1], "breed": row[2], "gender": row[3], "number_of_rides": row[4]})

        return response
    
