from extensions import db


class Didgit(db.Model):
    __tablename__ = 'Didgit'
    id = db.Column(db.Integer, primary_key=True)
    number_brut = db.Column(db.Double, nullable=False)
    valeur = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
