from django.urls import path
from . import views


app_name = 'reviews'

urlpatterns = [
    path('<int:movie_pk>/movie/create_review/', views.create_review, name='create_review'),
    path('<int:review_pk>/detail_review/', views.detail_review, name='detail_review'),
    path('<int:review_pk>/update_review/', views.update_review, name='update_review'),
    path('<int:review_pk>/delete_review/', views.delete_review, name='delete_review'),
    # path('<int:review_pk>/create_comment/', views.create_comment, name='create_comment'),
    # path('<int:review_pk>/review/<int:comment_pk>/comment/', views.delete_comment, name='delete_comment'),
]