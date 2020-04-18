from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # request lobby ID here
    path('instance/<int:lobbyId>/', views.lobby, name='lobby'),
]