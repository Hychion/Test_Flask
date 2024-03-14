from extensions import db

class Exigence(db.Model):
    __tablename__ = 'Exigence'
    id = db.Column(db.Integer, Foreignkey=True)
    competence_necessaire = db.Column(db.Integer, db.ForeignKey('Competence.id'), nullable=False)
    echeance = db.Column(db.Datetime)