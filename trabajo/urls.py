from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', producto2View, name='producto2'),
    path('logout', logout, name='logout'),
    path('login/', LoginView.as_view(template_name='trabajo/login.html'), name='login'),
    path('producto3/', producto3View, name='producto3'),
    path('producto4/', producto4View, name='producto4'),
    path('carro/', carroView, name='carro'),
    path('registarUsuario/', registrarUsuarioView, name='registro'),
]