# Importation des bibliothèques et modules nécessaires
from flask import Flask, render_template

from config import Config  # Paramètres de configuration
from extensions import db  # Extension de base de données

# Importation des differentes controllers
from controllers.eleves import eleves
from controllers.heure import h_m_s
from controllers.pdfDownload import pdf_download
from controllers.signup_login import auth_bp
from controllers.somme_des_chiffres import sum_way
from controllers.statistique import stat
from controllers.the_Good_number import game


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Chargement de la configuration de l'appli depuis la classe Config

    # Initialisation de la base de données avec l'application Flask
    db.init_app(app)

    # Enregistrement des différents blueprints pour la gestion des routes
    # Chaque blueprint représente un domaine fonctionnel différent de l'application
    app.register_blueprint(sum_way)
    app.register_blueprint(pdf_download)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(h_m_s)
    app.register_blueprint(eleves)
    app.register_blueprint(game)
    app.register_blueprint(stat)

    # Création de toutes les tables de base de données nécessaires
    # à l'intérieur du contexte de l'application Flask
    with app.app_context():
        db.create_all()

    # Définition de la route principale de l'application qui affiche la page d'accueil
    @app.route('/')
    def index():
        return render_template("endpoint_local/index.html")

    return app


# Point d'entrée de l'application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
