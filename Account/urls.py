from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.index, name='profile'),
    path('profile/games', views.user_games, name='user_games'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('registration', views.registration, name="registration"),
    path('edit', views.edit_account, name="edit_account"),
]