from flask import request, Response, Blueprint, session, render_template, url_for
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

    # Récupération du paramètre 'number' depuis la requête, avec 0 comme valeur par défaut
    number = request.args.get('number', default=0, type=int)

    if number < 0: # Vérification si le nombre est négatif
        # Préparation de la réponse XML en cas d'erreur
        return render_template("didgit.html",numbergiven=0,resultat=0)
    else:
        if session["user_id"] is None:
            return render_template(url_for('login'))
        else:
            print(session["user_id"])
            # Calcul de la somme des chiffres pour un nombre positif
            result = sum_didgit(number)

            # Creation d'une instance Difgit pour la mise en bdd
            new_number = Didgit(number_brut=number,
                                valeur=result,
                                user_id=6)

            db.session.add(new_number)
            db.session.commit()

            # Préparation de la réponse XML avec le résultat
            return render_template("didgit.html", numbergiven=number, resultat=result)

        return render_template('didgit.html')
