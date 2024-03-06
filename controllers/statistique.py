from flask import Blueprint, render_template

from extensions import db
from sqlalchemy.sql import func
import plotly.graph_objs as go
import plotly.offline as pyo

from models.game_score import Score_Game

stat = Blueprint("statistiques", __name__)


@stat.route('/top-users')
def top_users_view():
    top_users = get_top_users_by_requests()
    fig = create_top_users_graph(top_users)
    graph_html = pyo.plot(fig, include_plotlyjs=True, output_type='div')
    return render_template('statistique.html', graph_html=graph_html)


def get_top_users_by_requests():
    result = db.session.query(
        Score_Game.user_id, func.count(Score_Game.id).label('total_requests')
    ).group_by(
        Score_Game.user_id
    ).order_by(
        func.count(Score_Game.id).desc()
    ).limit(5).all()

    return result


def create_top_users_graph(top_users):
    user_ids = [str(user.user_id) for user in top_users]
    requests_counts = [user.total_requests for user in top_users]

    data = [go.Bar(x=user_ids, y=requests_counts)]
    layout = go.Layout(title='Top 5 utilisateurs par nombre de demandes')

    fig = go.Figure(data=data, layout=layout)
    return fig
