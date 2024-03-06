
from flask import Flask, render_template
from config import Config
from controllers.statistique import stat_graph
from controllers.the_Good_number import game
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
    app.register_blueprint(pdf_download)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(h_m_s)
    app.register_blueprint(eleves)
    app.register_blueprint(game)
    app.register_blueprint(stat_graph)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template("index.html")

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
