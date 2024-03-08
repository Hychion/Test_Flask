from flask import Blueprint, render_template, request

from extensions import db
from sqlalchemy.sql import func
import plotly.graph_objs as go
import plotly.offline as pyo

from models.game_score import Score_Game
from models.pdf_upload import PdfUpload

stat = Blueprint("statistiques", __name__)


@stat.route('/top-users', methods=["GET","POST"])
def top_users_view():
    top_users = get_top_users_by_requests()
    pdfupload = get_uploads_by_user()

    data_type = request.form.get('data_type', 'game_sessions')

    if data_type == "game_sessions":
        fig = create_top_users_graph(top_users)
    else:
        fig = create_top_upload_graph(pdfupload)

    graph_html = pyo.plot(fig, include_plotlyjs=True, output_type='div')
    return render_template('statistique.html', graph_html=graph_html)


def get_top_users_by_requests():
    result = db.session.query(
        Score_Game.user_id, func.count(Score_Game.id).label('totals_games')  # reference de la colones données
    ).group_by(
        Score_Game.user_id
    ).order_by(
        func.count(Score_Game.id).desc()
    ).limit(5).all()

    return result


def get_uploads_by_user():
    result = db.session.query(
        PdfUpload.user_id, func.count(PdfUpload.id).label('totals_uploads')  # reference de la colones données
    ).group_by(
        PdfUpload.user_id
    ).order_by(
        func.count(PdfUpload.id).desc()
    ).limit(5).all()
    return result


def create_top_users_graph(top_users):
    user_ids = [str(user.user_id) for user in top_users]
    requests_counts = [user.totals_games for user in top_users]

    data = [go.Bar(x=user_ids, y=requests_counts)]
    layout = go.Layout(title='Top 5 utilisateurs par nombre de demandes')

    fig = go.Figure(data=data, layout=layout)
    return fig


def create_top_upload_graph(upload_by_user):
    user_ids = [str(user.user_id) for user in upload_by_user]
    requests_counts = [user.totals_uploads for user in upload_by_user]  # Attention les labels utilisaient dans les
    data = [go.Bar(x=user_ids, y=requests_counts)]                      # requestes importe beaucoup

    layout = go.Layout(title='visualisation des uploads de pdf du top 5 utilisateurs ')
    fig = go.Figure(data=data, layout=layout)
    return fig
