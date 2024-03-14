from extensions import db

class Projet(db.Model):
    __tablename__ = 'Projet'
    id = db.Column(db.Integer, primary_key=True)
    sous_projets = db.Column(db.Integer, db.ForeignKey('sous_prjets.id'), nullable=False)
    date_de_debut = db.Column(db.DateTime)
    date_de_fin_prevue = db.Column(db.DateTime)
    date_de_fin_reelle = db.Column(db.DateTime)
    charge_prevue = db.Column(db.Integer)
    charge_reelle = db.Column(db.Integer)
    client = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable=False)
    satistfaction = db.Column(db.Integer)
    quantite = db.Column(db.Integer)
    avancement = db.Column(db.Integer)
