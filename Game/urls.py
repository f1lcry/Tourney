from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='games'),
    path('gamemode/<str:game_mode_name>', views.index, name='game_mode_list'),
    path('info/<int:game_pk>', views.index, name='game_info'),
]