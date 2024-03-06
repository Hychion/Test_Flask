from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from werkzeug.security import check_password_hash

from extensions import db
from models.user import User

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/singup', methods=['GET', 'POST'])
def singup():
    if session['user_id'] is not None:
        return render_template("index.html")

    if request.method == 'POST':
        data = request.form
        print(data)
        new_username = data.get('username')
        new_password = data.get('password')
        print("new_password"+new_password)

        if User.query.filter_by(username=new_username).first():
            return render_template("index.html", message="Ce nom d'utilisateur est déjà pris")

        new_user = User(username=new_username)
        new_user.set_password(new_password)

        session['user_id'] = new_user.get_id()

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
            return render_template("login.html", message="Identifiants incorrect")

        # Si la vérification est réussie, stocker l'id de l'utilisateur dans la session
        session['user_id'] = user.get_id()
        return render_template("index.html")
    return render_template("login.html")


@auth_bp.route('/logout')
def logout():
    print(session)
    session.pop('user_id', None)
    return redirect(url_for("auth_bp.login"))
