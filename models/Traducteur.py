from extensions import db


class Traducteur(db.Model):
    __tablename__ = 'Traducteur'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    email = db.Column(db.String)
    num_telephone = db.Column(db.String)
    competences = db.Column(db.Integer, db.ForeignKey("Competence.id"))
    vitesse_de_trad = 0 #toDO
    disponibilite = db.Column(db.Integer)
    disponibilite_debut = db.Column(db.Datetime)
    disponibilite_fin = db.Column(db.Datetime)

class Freelance(Traducteur):
    __tablename__ = 'Freelance'
    id = db.Column(db.Integer, primary_key=True)


class Tracducteur_salarie(Traducteur):
    __tablename__ = 'Freelance'
    id = db.Column(db.Integer, primary_key=True)
    work_shedule = db.Column(db.String)
