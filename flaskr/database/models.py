from flaskr.database.connection import db


class ChangeMe(db.Model):
    __tablename__ = "ChangeMe"

    id_car = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
