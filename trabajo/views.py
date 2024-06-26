from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import logout


#carrito
def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(id_producto = item[0])
        detalle.precio = item [3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        request.session["carro"] = []
    return redirect(to="carro")
        
def addtocar(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == id_producto:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
         carro.append([id_producto, producto.nombre_producto, producto.imagen,  producto.precio, 1, producto.precio ])
    request.session["carro"] = carro
    return redirect(to="carro")

def dropItem(request, id_producto):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == id_producto:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carro")

#para limpiar la lista
def limpiar(request, id_producto=None):
    if id_producto:
        carro = request.session.get("carro", [])

        for item in carro[:]: 
            if item[0] == id_producto:
                carro.remove(item)

        request.session["carro"] = carro
    else:
        request.session["carro"] = []
    return redirect(to="carro")

def carroView(request):
    return render(request,'trabajo/carro.html', {"carro": request.session.get("carro", [])})

#Registro
def registro(request):
    if request.method == "POST":
        registro = RegistroForm(request.POST)
        if registro.is_valid():
            registro.save()
            print("Registro exitoso...")
            return redirect(to="login")
    else:
        registro = RegistroForm()
    return render(request,'trabajo/registarUsuario.html',{'form': registro})
#logout

def logout_view(request):
    logout(request)
    print("Cerrando Sesion...")
    return redirect('producto2')

#Editor CRUD
#Productos
def editor(request):
    productos = Producto.objects.all()
    return render(request,'trabajo/Editor.html',{'productos': productos})

def productosAdd(request):
    if request.method == "POST":
        id_producto = request.POST["id_producto"]
        nombre_producto = request.POST["nombre_producto"]
        precio = request.POST["precio"]
        desc_producto = request.POST["desc_producto"]
        imagen = request.POST["imagen"]
        id_categoria = request.POST["id_categoria"]
        
        objCategoria = Categoria.objects.get(id_categoria=id_categoria)
        
        producto = Producto.objects.create(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            precio=precio,
            desc_producto=desc_producto,
            imagen=imagen,
            id_categoria=objCategoria
        )
        context = {'mensaje': "Ok, datos grabados..."}
        
        return redirect('productosAdd')
    
    else:
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'trabajo/productosAdd.html', context)

    
def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)
        
        producto.delete()
        mensaje="Bien, datos eliminados..."
        productos = Producto.objects.all()
        context={'productos':productos,'mensaje':mensaje}
        return render(request, 'trabajo/Editor.html',context)
    except:
        mensaje="Error, id no existe..."
        productos = Producto.objects.all()
        context={'productos':productos,'mensaje':mensaje}
        return render(request, 'trabajo/Editor.html',context)

def productos_findEdit(request, pk):
    if pk != "":
        producto = Producto.objects.get(id_producto=pk)
        categorias= Categoria.objects.all()
        
        print(type(producto.id_categoria.categoria))
        context={'producto':producto,'categorias':categorias}
        if producto:
            return render(request, 'trabajo/productos_findEdit.html',context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request, 'trabajo/Editor.html',context)

def productosUpdate(request):
    if request.method == "POST":
        id_producto = request.POST["id_producto"]
        nombre_producto = request.POST["nombre_producto"]
        precio = request.POST["precio"]
        desc_producto = request.POST["desc_producto"]
        imagen = request.POST["imagen"]
        id_categoria = request.POST["id_categoria"]
        
        objCategoria = Categoria.objects.get(id_categoria=id_categoria)
        
        producto = Producto.objects.update_or_create(
            id_producto=id_producto,
            defaults={
                'nombre_producto': nombre_producto,
                'precio': precio,
                'desc_producto': desc_producto,
                'imagen': imagen,
                'id_categoria': objCategoria,
            }
        )
        
        categorias = Categoria.objects.all()
        context = {'mensaje': "Ok, datos actualizados...", 'categorias': categorias, 'producto': producto}
        return render(request, 'trabajo/productos_findEdit.html', context)
    else:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'trabajo/Editor.html', context)
    
#Categorias
def crud_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    print("Enviando datos categorias_list")
    return render(request, 'trabajo/categorias_list.html', context)


def categoriasAdd(request):
    print("Estoy en controlador categoriasAdd...")
    context = {}
    
    if request.method == "POST":
        print("Controlador es un post...")
        form = CategoriaForm(request.POST)
        if form.is_valid():
            print("Estoy en agregar, is_valid")
            form.save()
            
            # Limpiar el formulario para un nuevo ingreso
            form = CategoriaForm()
            
            context = {'mensaje': "Ok, datos grabados..", 'form': form}
        else:
            context = {'form': form}
    else:
        form = CategoriaForm()
        context = {'form': form}
    
    return render(request, "trabajo/categorias_add.html", context)
            
def categorias_del(request,pk):
    mensaje={}
    errores={}
    categorias = Categoria.objects.all()
    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        context={}
        if categoria:
            categoria.delete()
            mensaje.append("Bien, datos eliminados...")
            context={'categorias':categorias,'mensaje':mensaje,'errores':errores}
            return render(request, "trabajo/categorias_list.html",context)
    except:
        print("Error, id no existe...")
        categorias=Categoria.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje,'categorias':categorias}
        return render(request, "trabajo/categorias_list.html",context)
    
def categorias_edit(request, pk):
    try:
        categoria = Categoria.objects.get(id_categoria=pk)  # Intenta obtener la categoría por su id
        mensaje = ""

        if request.method == "POST":
            # Si es una solicitud POST, procesa el formulario
            form = CategoriaForm(request.POST, instance=categoria)
            if form.is_valid():
                form.save()
                mensaje = "Categoría actualizada correctamente."
        else:
            form = CategoriaForm(instance=categoria)

        
        context = {'categoria': categoria, 'form': form, 'mensaje': mensaje}
        return render(request, "trabajo/categorias_edit.html", context)

    except Categoria.DoesNotExist:
        # Manejo de error si no se encuentra la categoría
        categorias = Categoria.objects.all()
        mensaje = "Error: La categoría no existe."
        context = {'categorias': categorias, 'mensaje': mensaje}
        return render(request, "trabajo/categorias_edit.html", context)
#Vistas

def producto2View(request):
    categoria_deseada = Categoria.objects.get(id_categoria=2) 
    productos = Producto.objects.filter(id_categoria=categoria_deseada)
    return render(request, 'trabajo/producto2.html', {'productos': productos, "carro":request.session.get("carro", [])})

def producto3View(request):
    categoria_deseada = Categoria.objects.get(id_categoria=1) 
    productos = Producto.objects.filter(id_categoria=categoria_deseada)
    return render(request, 'trabajo/producto3.html', {'productos': productos, "carro":request.session.get("carro", [])})
    
def producto4View(request):
    categoria_deseada = Categoria.objects.get(id_categoria=3) 
    productos = Producto.objects.filter(id_categoria=categoria_deseada)
    return render(request, 'trabajo/producto4.html', {'productos': productos, "carro":request.session.get("carro", [])})
#base.html

def baseView(request):
    return render(request, 'trabajo/base.html')
