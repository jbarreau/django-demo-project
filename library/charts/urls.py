from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


app_name = "library"

urlpatterns = [
    path(
        "/exemple-value",
        csrf_exempt(views.ValueChartView.as_view()),
        name="exemple-value",
    ),
    path(
        "/exemple-pie",
        csrf_exempt(views.PieChartView.as_view()),
        name="exemple-pie",
    ),
    path(
        "/exemple-line",
        csrf_exempt(views.LineChartView.as_view()),
        name="exemple-line",
    ),
    path(
        "/exemple-objective",
        csrf_exempt(views.ObjectiveChartView.as_view()),
        name="exemple-objective",
    ),
    path(
        "/exemple-leaderboard",
        csrf_exempt(views.LeaderBoardChartView.as_view()),
        name="exemple-leaderboard",
    ),

    path(
        "/nb_book_category",
        csrf_exempt(views.NbBookByCategoryChartView.as_view()),
        name="nb_book_category",
    ),
]
