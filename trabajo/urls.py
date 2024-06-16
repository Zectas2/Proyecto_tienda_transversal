from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto2View, name='producto2'),
    path('producto3/', views.producto3View, name='producto3'),
    path('producto4/', views.producto4View, name='producto4'),
    path('registarUsuario/', views.registrarUsuarioView, name='registro'),
]