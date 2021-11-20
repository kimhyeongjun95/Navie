from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),
    # path('<int:movie_pk>/detail_movie', views.detail_movie, name='detail_movie'),
]