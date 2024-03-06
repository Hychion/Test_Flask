from datetime import datetime

from flask import render_template, Blueprint

h_m_s = Blueprint("heure", __name__)

@h_m_s.route('/heure')
def heure():
    date_local = datetime.now()
    h = date_local.hour
    m = date_local.minute
    s = date_local.second
    return render_template("heure.html", heure=h, minute=m, seconde=s)
