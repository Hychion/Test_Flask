import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from config import Config
from extensions import db

from controllers.eleves import eleves
from controllers.heure import h_m_s
from controllers.pdfDownload import pdf_download
from controllers.signup_login import auth_bp
from controllers.somme_des_chiffres import sum_way


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(sum_way)
    app.register_blueprint(pdf_download, url_prefix='/pdf')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(h_m_s)
    app.register_blueprint(eleves)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        # print('Chemin absolu vers templates:', os.path.abspath('templates'))
        # print('Chemin de template_folder:', app.template_folder)
        # print('Chemin de recherche de templates:', app.jinja_loader.searchpath)
        return render_template("index.html")

    """
    @app.before_request
    def test_db_connection():
        try:
            # Utilise db.session.execute pour exécuter une requête simple
            db.session.execute(text('SELECT 1'))
            db.session.commit()  # Assurez-vous de commit si nécessaire
            print('Connexion à la base de données réussie.')
        except Exception as e:
            print('Erreur lors de la connexion à la base de données:', e)
    """

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
