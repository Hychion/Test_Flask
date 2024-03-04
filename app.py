import zoneinfo

from flask import Flask, render_template

import datetime

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


if __name__ == '__main__':
    app.run()
