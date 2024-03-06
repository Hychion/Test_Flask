import plotly.graph_objs as go
import plotly.offline as pyo

from flask import Blueprint, render_template, Request, session, redirect, url_for
from sqlalchemy import func, desc

from extensions import db
from models.user import User


stat_graph = Blueprint("statistiques", __name__)


@stat_graph.route('/statistiques')
def statistiques():
    if session.get("user_id") is None:
        return redirect(url_for('auth_bp.login'))

    top_users = db.session.query(User.id, func.count(Request.id).label('didgit')) \
        .join(Request, User.id == Request.user_id) \
        .group_by(User.name) \
        .order_by(desc('total_requests')) \
        .limit(5).all()

    plot_div = create_plot(top_users)
    return render_template("statistiques.html", plot_div=plot_div)

    return render_template('heure.html')


def create_plot(top_users):
    data = [
        go.Bar(
            x=[user.name for user in top_users],  # Noms des utilisateurs
            y=[user.total_requests for user in top_users]  # Total des demandes
        )
    ]

    layout = go.layout(title="top 5 des utilisateurs ayant fait le plus de demandes ",
                       x=dict(title="Utilisateurs"),
                       y=dict(titel="Nombre de demande")
                    )
    figure = go.Figure(data=data, layout=layout)

    return pyo.plot(figure, output_type="div", include_plotyjs=False)
