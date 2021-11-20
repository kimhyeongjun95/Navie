from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search_info/', views.search_info, name='search_info'),
    path('<int:user_pk>/searched_id/', views.searched_id, name='searched_id'),
    path('<int:user_pk>/password/', views.search_change_password, name='search_change_password'),
    path('<user_username>/profile/', views.profile, name='profile'),
    path('<int:user_pk>/change_personal_info/', views.change_personal_info, name='change_personal_info'),
    path('<int:user_pk>/delete_user/', views.delete_user, name='delete_user'),
    path('password/', views.change_password, name="change_password"),
]