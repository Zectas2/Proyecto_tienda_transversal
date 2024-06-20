from django.shortcuts import render,redirect
from .models import *

from django.shortcuts import render
from .models import Producto, Categoria


#carrito
def carroView(request):
    context = {}
    return render(request,'trabajo/carro.html', context)

#Vistas

#Login
def loginView(request):
    context = {
        'clases': [
            'navbar',
            'animation',
            'start-home',
            'container-cart-icon',
            'container-cart-products',
            'hidden-cart',
            'row-product',
            'cart-product',
            'info-cart-product',
            'cantidad-producto-carrito',
            'titulo-producto-carrito',
            'precio-producto-carrito',
            'cart-total',
            'total-pagar',
            'cart-empty',
            'container-items',
            'item',
            'info-product',
            'valorObjeto',
            'simboloMoneda',
            'price',
            'btn-add-cart',
            'coinversor',#22
            'coinversor-icon',
            'comvertirPrecio',
            'hidden',#25
            'contactanos',
            'contenerdorMain',
            'formulario',
            'contenedor-campos',
            'campo',
            'alinear-abajo',
            'boton',
            'labelForm',
        ]}
    return render(request,'trabajo/login.html', context)

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
    return render(request, 'trabajo/producto3.html', {'productos': productos})

def registrarUsuarioView(request):
    context = {
        'clases': [
            'navbar',
            'animation',
            'start-home',
            'container-cart-icon',
            'container-cart-products',
            'hidden-cart',
            'row-product',
            'cart-product',
            'info-cart-product',
            'cantidad-producto-carrito',
            'titulo-producto-carrito',
            'precio-producto-carrito',
            'cart-total',
            'total-pagar',
            'cart-empty',
            'container-items',
            'item',
            'info-product',
            'valorObjeto',
            'simboloMoneda',
            'price',
            'btn-add-cart',
            'coinversor',
            'coinversor-icon',
            'comvertirPrecio',
            'hidden',#25
            'contactanos',
            'contenerdorMain',
            'formulario',
            'contenedor-campos',
            'campo',
            'alinear-abajo',
            'boton',
            'labelForm',
        ]
        
    }
    return render(request, 'trabajo/registarUsuario.html', context)
#base.html
def baseView(request):
    return render(request, 'trabajo/base.html', context)

