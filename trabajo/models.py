from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
#Creamos la clases Venta para almacenar el registro de ventas
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    def __str__(self):
        return "id:"+str(self.id) +" Nc:"+ self.cliente.username+" F:"+str(self.fecha)
        
    
    

    
# Creamos la clase Categoria
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=4,db_column='idCategoria',primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return f"id:{self.id_categoria} - N:{self.categoria}"

# Cresmos la Clase Producto
class Producto(models.Model):
    id_producto = models.CharField(max_length=4,primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    desc_producto = models.CharField(max_length=20)
    imagen = models.CharField(max_length=400, blank=True)
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    
    def __str__(self):
        return f"id:{self.id_producto} - N:{self.nombre_producto} ({self.id_categoria})"


#creamos la clase detalle para guardar los datos de cada venta
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    def __str__(self):
        return "id:"+str(self.id) +" N:"+self.producto.nombre_producto[0:12]+" idV:"+str(self.venta.id)
    
#python manage.py makemigrations
#python manage.py migrate

#python manage.py runserver

#python manage.py createsuperuser
#Paso 2: Username: admin
#Paso 3: Email address: admin@example.com
#Paso 4: Agregar contraseña
