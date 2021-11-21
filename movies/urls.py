from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),
    path('<int:movie_pk>/detail_movie', views.detail_movie, name='detail_movie'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('recommend_movies/', views.recommend_movies, name='recommend_movies'),
    path('movies_worldcup/', views.movies_worldcup, name='movies_worldcup'),
    path('<int:movie1_pk>/<int:movie2_pk>/result_recommend/', views.result_recommend, name='result_recommend'),
]