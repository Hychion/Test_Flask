import datetime
import tempfile

from flask import request, jsonify, Blueprint, render_template, session
import fitz  # PyMuPDF
import os

from extensions import db
from models.pdf_upload import PdfUpload

pdf_download = Blueprint('pdf_download', __name__)


@pdf_download.route('/upload_pdf', methods=['GET', 'POST'])
def upload_pdf() -> jsonify:
    if request.method == 'POST':
        print(session["user_id"])
        if 'pdf' not in request.files:  # verification de recuperation de fichier non vide
            return render_template("UploadPdf.html", message="Pas de fichier selectionner")

        file = request.files["pdf"]

        if file.filename == '':  # verification
            return render_template("UploadPdf.html", message="Fichier sans nom !!")

        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(tempfile.gettempdir(), file.filename)
            file.save(filepath)
            # Extraction du text provenant du PDF
            text = extract_text_from_pdf(filepath)
            # Compter les mots
            word_count = count_word(text)
            # suppresion du fichier temporaire

            session['words_pdf'] = word_count

            new_pdf = PdfUpload(filename=file.filename,
                                word_count=word_count,
                                user_id=session['user_id']
                                )


            db.session.add(new_pdf)
            db.session.commit()
            os.remove(filepath)

            return render_template("UploadPdf.html", message="Ok")
        else:
            return render_template("UploadPdf.html", message="Fichier du movais type")
    else:
        return render_template("UploadPdf.html")


def extract_text_from_pdf(filepath: str) -> str:
    text = ""
    with fitz.open(filepath) as pdf_text:
        for page in pdf_text:
            text += page.get_text()
    return text


def count_word(text: str) -> int:
    words = text.split(" ")
    return len(words)
