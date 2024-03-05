from flask import Blueprint, request, jsonify, session, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models.user import User

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/singup', methods=['GET', 'POST'])
def singup():
    if request.method == 'POST':
        data = request.form
        print(data)
        new_username = data.get('username')
        new_password = data.get('password')
        print("new_password"+new_password)
        if User.query.filter_by(username=new_username).first():
            return jsonify({'message': "Ce nom d'utilisateur est déjà pris"}), 400

        new_user = User(username=new_username)
        new_user.set_password(new_password)
        db.session.add(new_user)
        db.session.commit()

        return render_template("index.html")
    return render_template("singup.html")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        print(data)

        username = data.get('username')
        password = data.get('password')

        # Vérifier si l'utilisateur existe
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"message": "Nom d'utilisateur ou mot de passe invalide."}), 401

        # Si la vérification est réussie, stocker l'id de l'utilisateur dans la session
        session['user_id'] = user.id
        return jsonify({"message": "Connexion réussie."}), 200
    return render_template("login.html")


@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Déconnexion réussie."}), 200
