from extensions import db
from enum import Enum


class Langue(Enum):
    __tablename__ = "Langue"
    FRANCAIS = "Francais"
    ANGLAIS = "Anglais"
    ALLEMAND = "Allemand"
    ESPAGNOL = "Espagnol"
    NEERLANDAIS = "Néerlandais"
    ITALIEN = "Italien"
