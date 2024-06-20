from django.urls import path
from . import views
#from django.contrib.auth.views import loginView

urlpatterns = [
    path('', views.producto2View, name='producto2'),
    path('login/', views.loginView, name='login'),
    path('producto3/', views.producto3View, name='producto3'),
    path('producto4/', views.producto4View, name='producto4'),
    path('carro/', views.carroView, name='carro'),
    path('registarUsuario/', views.registrarUsuarioView, name='registro'),
]