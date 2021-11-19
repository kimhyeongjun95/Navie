from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('search_info/', views.search_info, name='search_info'),
    path('searched_id/', views.searched_id, name='searched_id'),
    path('logout/', views.logout, name='logout'),
    path('password/', views.change_password, name='change_password'),  
    # path('<username>/', views.profile, name='profile'),
    path('change_personal_info/', views.change_personal_info, name='change_personal_info'),
]