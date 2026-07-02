from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_games, name="all_games"),
    path("top-sales/", views.get_top_sales, name="top_sales",),
    path("genre/<str:genre>/", views.get_games_by_genre, name="games_by_genre"),
    path("platform/<str:platform>/", views.get_games_by_platform, name="games_by_platform"),
    path("publisher/<str:publisher>/", views.get_games_by_publisher, name="games_by_publisher"),
    path("add/", views.add_game, name="add_game"),
    path("form/", views.game_form, name="game_form"),
]