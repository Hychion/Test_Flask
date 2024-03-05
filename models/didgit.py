from extensions import db


class didgit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valeur = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
