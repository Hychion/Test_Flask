from random import randint

from flask import request, session, render_template, Blueprint, url_for, redirect

from extensions import db
from models.game_score import Score_Game

# Création d'un blueprint 'the_good_page' pour le jeu
game = Blueprint("the_good_page", __name__)


# Route '/jeu' accessible en GET pour commencer le jeu et en POST pour soumettre une réponse
@game.route('/jeu', methods=["GET", "POST"])
def jeu():

    if session.get("user_id") is None:
        return redirect(url_for('auth_bp.login'))
    # Traitement des soumissions de l'utilisateur
    if request.method == "POST":

        # Récupération du nombre proposé par l'utilisateur
        reponse = int(request.form.get('nombre'))
        # Enregistrement de la tentative dans la session
        session['essais'].append(reponse)

        # Vérification de la réponse de l'utilisateur par rapport au nombre mystère
        if reponse == session['nb']:
            session['en_cours'] = False
            message = "Bravo, c'est gagné !"
            #  Ajout des résultats en Bdd
            add_Score()

        elif reponse < session['nb']:
            message = "Non, c'est plus !"
        else:
            message = "Non, c'est moins !"

        # Décrémentation du nombre d'essais restants
        session['nb_essais'] = session['nb_essais'] - 1

        # Vérification si le joueur a épuisé tous ses essais
        if session['nb_essais'] == 0:
            session['en_cours'] = False
            message = "C'est perdu !"
            #  Ajout des résultats en Bdd
            add_Score()

        print(session)

        # Retour du template du jeu avec un message (résultat de la tentative)
        return render_template('endpoint_local/game.html', message=message)

    else:  # Initialisation du jeu pour une requête GET
        nb_mystere = randint(0, 100)  # Génération d'un nombre aléatoire entre 0 et 100
        # Initialisation des variables de session pour le jeu
        session['nb'] = nb_mystere
        session['en_cours'] = True
        session['nb_essais'] = 10
        session['essais'] = []
        print(session)

        # Affichage du formulaire de jeu au début
        return render_template('endpoint_local/game.html')


def add_Score():

    if 10 - session['nb_essais'] == 0:
        status = "Loose"
    else:
        status = "Win"

    score = Score_Game(
        user_id=session['user_id'],
        nb_essais=10 - session['nb_essais'],
        etat=status
    )
    db.session.add(score)
    db.session.commit()
