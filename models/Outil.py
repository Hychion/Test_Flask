from extensions import db
from sqlalchemy import Enum as SQlAlchemyEnum

from models import Langue, Domaine


class Outil(db.Model):
    __teblename__ = "Outil"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
