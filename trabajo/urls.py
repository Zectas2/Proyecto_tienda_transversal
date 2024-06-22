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
    path('editor/', editor, name='editor'),
    path('productosAdd', productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>', productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', productosUpdate, name='productosUpdate'),
    
    path('crud_categorias', crud_categorias, name='crud_categorias'),
    path('categoriasAdd', categoriasAdd, name='categoriasAdd'),
    path('categorias_del/<str:pk>', categorias_del, name='categorias_del'),
    path('categorias_edit/<str:pk>', categorias_edit, name='categorias_edit'),
]