from extensions import db

from enum import Enum


class Domaine(Enum):
    __tablename__ = "Domaine"
    MEDICAL = "Médical"
    JURIDIQUE = "Juridique"
    TECHONLOGIQUE = "Technologique"
