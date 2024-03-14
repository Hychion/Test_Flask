from extensions import db

class Project_Manager(db.Model):
    __tablename__="Project_Manager"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    email = db.Column(db.String)
    num_telephone = db.Column(db.String)
    projets = db.Column(db.Integer, db.ForeignKey("Projet.id"))

    manage = db.Column(db.Integer, db.ForeignKey("Traducteur_salarie.id"))
    peut_contacter = db.Column(db.Integer, db.ForeignKey("Freelance.id"))
