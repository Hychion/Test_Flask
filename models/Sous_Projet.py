from extensions import db



class Sous_Projet(db.Model):
    __tablename__ = 'Sous_Projet'
    id = db.Column(db.Integer, primary_key=True)
    date_de_debut = Column(db.DateTime)
    date_de_fin_prevue = Column(db.DateTime)
    charge_prevue = db.Column(db.Integer)
    charge_reelle = db.Column(db.Integer)
    tache = db.Column(db.Integer, db.ForeignKey('Tache.id'))
    categorie = db.Column(db.Integer, db.ForeignKey('Categorie.id'), nullable=False)
    sous_projet_requis = db.Column(db.Integer, db.ForeignKey('Sous_projet.id'))
    sous_projet_suivant = db.Column(db.Integer, db.ForeignKey('Sous_projet.id'))
    quantite = db.Column(db.Integer)
    avancement = db.Column(db.Integer)

    exigence = db.Column(db.Integer, db.ForeignKey('Exigence.id'))
