from random import randint

from flask import request, session, render_template, Blueprint

game = Blueprint("the_good_page", __name__)

@game.route('/jeu', methods=["GET", "POST"])
def jeu():
    if request.method == "POST":
        reponse = int(request.form.get('nombre'))
        session['essais'].append(reponse)
        if reponse == session['nb']:
            session['en_cours'] = False
            message = "Bravo, c'est gagné !"
        elif reponse < session['nb']:
            message = "Non, c'est plus !"
        else:
            message = "Non, c'est moins !"

        session['nb_essais'] = session['nb_essais'] - 1

        if session['nb_essais'] == 0:
            session['en_cours'] = False
            message = "C'est perdu !"
        print(session)
        return render_template('game.html', message=message)

    else:
        nb_mystere = randint(0, 100)
        session['nb'] = nb_mystere
        session['en_cours'] = True
        session['nb_essais'] = 10
        session['essais'] = []
        print(session)
        # affichage du formulaire
        return render_template('game.html')
