from extensions import db

class Tache(db.Model):
    __tablename__ = "Tache"
    id = db.Column(db.Integer,  primary_key=True)
    intitule = db.Column(db.String)
    exigence = db.Column(db.Integer, db.Foreignkey("Exigence.id"))
    date_de_debut = db.Column(db.DateTime)
    date_de_fin = db.Column(db.DateTime)
    charge_prevue = db.Column(db.Integer)
    charge_reelle = db.Column(db.Integer)
    quantite = db.Column(db.Integer)
    avancement = db.Column(db.Integer)
    sous_taches = db.Column(db.Integer, db.Foreignkey("Tache.id")) ##Se divise


