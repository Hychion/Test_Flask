from extensions import db

class Categorie(db.Model):
    __tablename__ = 'Categorie'
    id = db.Column(db.Integer)
    nom = db.Column(db.String)
