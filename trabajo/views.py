from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.views import logout_then_login

#logout
def logout(request):
    return logout_then_login(request,login_url='login')
#carrito
def carroView(request):
    return render(request,'trabajo/carro.html')

#Vistas



def producto2View(request):
    categoria_deseada = Categoria.objects.get(id_categoria=2) 
    productos = Producto.objects.filter(id_categoria=categoria_deseada)
    return render(request, 'trabajo/producto2.html', {'productos': productos})

def producto3View(request):
    categoria_deseada = Categoria.objects.get(id_categoria=1) 
    productos = Producto.objects.filter(id_categoria=categoria_deseada)
    return render(request, 'trabajo/producto3.html', {'productos': productos})
    
def producto4View(request):
    categoria_deseada = Categoria.objects.get(id_categoria=3) 
    productos = Producto.objects.filter(id_categoria=categoria_deseada)
    return render(request, 'trabajo/producto4.html', {'productos': productos})

def registrarUsuarioView(request):
    return render(request, 'trabajo/registarUsuario.html')
#base.html
def baseView(request):
    return render(request, 'trabajo/base.html')

