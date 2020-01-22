from application import db

class Horse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    breed = db.Column(db.String(144), nullable=True)
    skill_level = db.Column(db.String(50), nullable=False)

    def __init__(self, name, gender, breed, skill_level):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.skill_level = skill_level

