from flask import request, Blueprint, session, render_template, url_for, redirect
from extensions import db
from models.didgit import Didgit

# Création d'un blueprint 'somme_des_chiffres'
sum_way = Blueprint('somme_des_chiffres', __name__)


# Fonction pour calculer la somme des chiffres d'un nombre
def sum_didgit(number: int) -> int:
    return sum(int(digit) for digit in str(number))


# Outil de conversion de la response serveur en XML
# Version renvoie d'xml
def dict_to_xml(tag, d):
    parts = [f'<{tag}>']  # Début du tag XML
    for key, val in d.items():  # Pour chaque paire clé/valeur dans le dictionnaire
        parts.append(f'<{key}>{val}</{key}>')  # Ajout de la paire sous forme de balises XML
    parts.append(f'</{tag}>')  # Fermeture du tag XML
    return ''.join(parts)  # Assemblage et retour de la chaîne XML


# Définition de la route '/sum_didgit' accessible en GET
# Cas d'utilisation : http://localhost:5000/sum_didgit?number=123
@sum_way.route('/sum_didgit')
def request_sum_of_didgit():
    number = request.args.get('number', default=0, type=int)

    if session.get("user_id") is None:
        return redirect(url_for('login'))  # Assurez-vous d'importer `redirect`
    else:
        print(session["user_id"])
        resultat = sum_didgit(number) if number > 0 else 0

        if number > 0:
            new_number = Didgit(number_brut=number,
                                valeur=resultat,
                                user_id=session['user_id'])
            db.session.add(new_number)
            db.session.commit()

        return render_template("didgit.html", number=number, resultat=resultat)