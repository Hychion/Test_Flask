from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "id : " + self.id + "; password " + self.password

    def get_username(self):
        return self.username

    def get_id(self):
        return self.id
