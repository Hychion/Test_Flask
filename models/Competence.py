from extensions import db
from sqlalchemy import Enum as SQlAlchemyEnum

from models import Langue, Domaine


class Competence(db.Model):
    __teblename__ = "Competence"
    id = db.Column(db.Integer, primary_key=True)
    langue_source = db.Column(db.Integer, db.ForeignKey('Langue.id'))
    langue_cible = db.Column(SQlAlchemyEnum(Langue)) # TODO je ne sais pas si ca fonctionne
    outil = db.Column(db.Integer, db.Foreignkey("Outil.id"))
    domaine = db.Column(SQlAlchemyEnum(Domaine))
