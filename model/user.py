from app import db


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255),nullable=False)