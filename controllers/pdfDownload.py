
import tempfile

from flask import request, jsonify, Blueprint, render_template, session, redirect, url_for
import fitz  # PyMuPDF
import os

from extensions import db
from models.pdf_upload import PdfUpload

# Déclaration d'un nouveau blueprint pour les téléchargements de PDF
pdf_download = Blueprint('pdf_download', __name__)


@pdf_download.route('/upload_pdf', methods=['GET', 'POST'])
def upload_pdf() -> jsonify:
    if session.get("user_id") is None:
        return redirect(url_for('auth_bp.login'))
    if request.method == 'POST':  # Vérification de la présence du fichier dans la requête
        print(session["user_id"])
        if 'pdf' not in request.files:  # verification de recuperation de fichier non vide
            return render_template("UploadPdf.html", message="Pas de fichier selectionner")

        file = request.files["pdf"]

        if file.filename == '':  # Vérification que le fichier a un nom
            return render_template("UploadPdf.html", message="Fichier sans nom !!")

        if file and file.filename.endswith('.pdf'):  # Vérification de l'extension du fichier

            filepath = os.path.join(tempfile.gettempdir(), file.filename)
            file.save(filepath)

            # Extraction du texte du PDF
            text = extract_text_from_pdf(filepath)
            # Comptage des mots dans le texte extrait
            word_count = count_word(text)

            session['words_pdf'] = word_count

            # Création d'une nouvelle instance PdfUpload pour enregistrement en base de données
            new_pdf = PdfUpload(filename=file.filename,
                                word_count=word_count,
                                user_id=session['user_id']
                                )

            db.session.add(new_pdf)  # Ajout de l'instance à la session de la base de données
            db.session.commit()  # Enregistrement des modifications
            os.remove(filepath)  # suppresion du pdf

            return render_template("UploadPdf.html", message="Ok")
        else:
            return render_template("UploadPdf.html", message="Fichier du movais type")
    else:
        return render_template("UploadPdf.html")


def extract_text_from_pdf(filepath: str) -> str:
    # Fonction pour extraire le texte d'un fichier PDF
    text = ""
    with fitz.open(filepath) as pdf_text:  # Ouverture du fichier PDF avec PyMuPDF
        for page in pdf_text:  # Parcours des pages du PDF
            text += page.get_text()  # Extraction et ajout du texte de chaque page
    return text


def count_word(text: str) -> int:
    # Fonction pour compter le nombre de mots dans un texte
    words = text.split(" ")  # Séparation du texte en mots
    return len(words)  # Retour du nombre de mots
