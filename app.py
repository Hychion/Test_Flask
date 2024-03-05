import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config

from controllers.eleves import eleves
from controllers.heure import h_m_s
from controllers.pdfDownload import pdf_download
from controllers.signup_login import auth_bp
from controllers.somme_des_chiffres import sum_way

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(sum_way)
    app.register_blueprint(pdf_download, url_prefix='/pdf')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(h_m_s)
    app.register_blueprint(eleves)

    @app.route('/')
    def index():
        # print('Chemin absolu vers templates:', os.path.abspath('templates'))
        # print('Chemin de template_folder:', app.template_folder)
        # print('Chemin de recherche de templates:', app.jinja_loader.searchpath)

        return render_template("index.html")

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
