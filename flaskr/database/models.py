from flaskr.database.connection import db


class VuttrModel(db.Model):
    __tablename__ = "vuttr"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    tags = db.Column(db.String(255), nullable=False)
