from extensions import db


class Score_Game(db.Model):
    __tablename__= 'Score_Game'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    nb_essais = db.Column(db.Integer, nullable=False)
    etat = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
