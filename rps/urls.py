from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start-game/', views.game, name='start_game'),
    path('result/', views.result, name='result'),
]
