from flask import Flask, render_template
import datetime

from controller.pdfDownload import pdf_download
from controller.somme_des_chiffres import sum_way

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/heure')
def heure():
    date_local = datetime.datetime.now()
    h = date_local.hour
    m = date_local.minute
    s = date_local.second
    return render_template("heure.html", heure=h, minute=m, seconde=s)

@app.route('/pdf')
def to_uploadpdf():
    return render_template("UploadPdf.html")


app.register_blueprint(sum_way)
app.register_blueprint(pdf_download)

if __name__ == '__main__':

    app.run(debug=True)
