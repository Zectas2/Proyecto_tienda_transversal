from django.shortcuts import render
from .models import Categoria,Producto
#Vistas

def producto2View(request):
    context = {
        'clases': [
            'navbar',#0
            'animation',
            'start-home',
            'container-cart-icon',
            'container-cart-products',
            'hidden-cart',#5
            'row-product',
            'cart-product',
            'info-cart-product',
            'cantidad-producto-carrito',
            'titulo-producto-carrito',#10
            'precio-producto-carrito',
            'cart-total',
            'total-pagar',
            'cart-empty',
            'container-items',#15
            'item',
            'info-product',
            'valorObjeto',
            'simboloMoneda',
            'price',#20
            'btn-add-cart',
            'coinversor',
            'coinversor-icon',
            'comvertirPrecio',
            'hidden',#25
            'contactanos',
        ]
    }
    return render(request, 'trabajo/producto2.html', context)

def producto3View(request):
    context = {
        'clases': [
            'navbar',#0
            'animation',
            'start-home',
            'container-cart-icon',
            'container-cart-products',
            'hidden-cart',#5
            'row-product',
            'cart-product',
            'info-cart-product',
            'cantidad-producto-carrito',
            'titulo-producto-carrito',#10
            'precio-producto-carrito',
            'cart-total',
            'total-pagar',
            'cart-empty',
            'container-items',#15
            'item',
            'info-product',
            'valorObjeto',
            'simboloMoneda',
            'price',#20
            'btn-add-cart',
            'coinversor',
            'coinversor-icon',
            'comvertirPrecio',
            'hidden',#25
            'contactanos',
        ]
    }
    return render(request, 'trabajo/producto3.html', context)
    
def producto4View(request):
    context = {
        'clases': [
            'navbar',#0
            'animation',
            'start-home',
            'container-cart-icon',
            'container-cart-products',
            'hidden-cart',#5
            'row-product',
            'cart-product',
            'info-cart-product',
            'cantidad-producto-carrito',
            'titulo-producto-carrito',#10
            'precio-producto-carrito',
            'cart-total',
            'total-pagar',
            'cart-empty',
            'container-items',#15
            'item',
            'info-product',
            'valorObjeto',
            'simboloMoneda',
            'price',#20
            'btn-add-cart',
            'coinversor',
            'coinversor-icon',
            'comvertirPrecio',
            'hidden',#25
            'contactanos',
        ]
    }
    return render(request, 'trabajo/producto4.html', context)
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
            'hidden',
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
    context = {
        'clases': [
            'navbar',#0
            'animation',
            'start-home',
            'container-cart-icon',
            'container-cart-products',
            'hidden-cart',#5
            'row-product',
            'cart-product',
            'info-cart-product',
            'cantidad-producto-carrito',
            'titulo-producto-carrito',#10
            'precio-producto-carrito',
            'cart-total',
            'total-pagar',
            'cart-empty',
            'container-items',#15
            'item',
            'info-product',
            'valorObjeto',
            'simboloMoneda',
            'price',#20
            'btn-add-cart',
            'coinversor',
            'coinversor-icon',
            'comvertirPrecio',
            'hidden',#25
            'contactanos',
        ]
    }
    return render(request, 'trabajo/base.html', context)

#Consultasw de Datos
def index(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render(request, 'productos/index.html', context)