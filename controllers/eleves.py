from flask import render_template, Blueprint, request

eleves = Blueprint("eleves", __name__)

liste_eleves = [
    {'nom': 'Dupont', 'prenom': 'Jean', 'classe': '2A'},
    {'nom': 'Dupont', 'prenom': 'Jeanne', 'classe': 'TG2'},
    {'nom': 'Marchand', 'prenom': 'Marie', 'classe': '2A'},
    {'nom': 'Martin', 'prenom': 'Adeline', 'classe': '1G1'},
    {'nom': 'Dupont', 'prenom': 'Lucas', 'classe': '2A'}
]


# TO TEST http://127.0.0.1:5000/eleves?c=2A
@eleves.route("/eleves")
def get_eleves():
    classe = request.args.get('c')
    if classe:
        eleves_selectionnes = [eleve for eleve in liste_eleves if eleve['classe'] == classe]
    else:
        eleves_selectionnes = []
    return render_template("eleves.html", eleves=eleves_selectionnes)
