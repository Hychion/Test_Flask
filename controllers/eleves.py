from flask import render_template, Blueprint, request

# Création d'un blueprint 'eleves' pour regrouper les routes liées aux élèves
eleves = Blueprint("eleves", __name__)


# Liste simulée d'élèves pour l'exemple
liste_eleves = [
    {'nom': 'Dupont', 'prenom': 'Jean', 'classe': '2A'},
    {'nom': 'Dupont', 'prenom': 'Jeanne', 'classe': 'TG2'},
    {'nom': 'Marchand', 'prenom': 'Marie', 'classe': '2A'},
    {'nom': 'Martin', 'prenom': 'Adeline', 'classe': '1G1'},
    {'nom': 'Dupont', 'prenom': 'Lucas', 'classe': '2A'}
]


# Définition de la route '/eleves' accessible par HTTP GET
# Cas d'utilisation : http://127.0.0.1:5000/eleves?c=2A pour filtrer par classe
@eleves.route("/eleves")
def get_eleves():
    classe = request.args.get('c') # Recuperation de l'argument mis en parametre dans url ?c=...

    # Filtrage des élèves appartenant à la classe spécifiée si 'classe' est fourni
    if classe:
        eleves_selectionnes = [eleve for eleve in liste_eleves if eleve['classe'] == classe]

    else:  # Si aucun paramètre 'c' n'est fourni, la liste des élèves sélectionnés est vide
        eleves_selectionnes = []

    # Rendu du template 'eleves.html' en passant la liste filtrée des élèves
    return render_template("eleves.html", eleves=eleves_selectionnes)
