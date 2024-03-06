from extensions import db


class Didgit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_brut = db.Column(db.Integer, nullable=False)
    valeur = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
