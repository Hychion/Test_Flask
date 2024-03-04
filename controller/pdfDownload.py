import tempfile

from flask import Flask, request, jsonify, Blueprint
import fitz  # PyMuPDF
import os

pdf_download = Blueprint('pdf_download', __name__)


@pdf_download.route('/upload-pdf', methods=['POST'])
def upload_pdf() -> jsonify:
    if 'pdf' not in request.files:  # verification de recuperation de fichier non vide
        return jsonify({"error": "No fil part"}), 400

    file = request.files["pdf"]

    if file.filename == '':  # verification
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(tempfile.gettempdir(), file.filename)
        file.save(filepath)
        # Extraction du text provenant du PDF
        text = extract_text_from_pdf(filepath)
        # Compter les mots
        word_count = count_word(text)
        # suppresion du fichier temporaire
        os.remove(filepath)
        return jsonify({"word_count": word_count})
    else:
        return jsonify({"error": "Invalid file type"}), 400


def extract_text_from_pdf(filepath: str) -> str:
    text = ""
    with fitz.open(filepath) as pdf_text:
        for page in pdf_text:
            text += page.get_text()
    return text


def count_word(text: str) -> int:
    words = text.split(" ")
    return len(words)
