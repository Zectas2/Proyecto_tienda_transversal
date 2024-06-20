from django.db import models

# Create your models here.
# Creamos la clase Categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return f"{self.id_categoria} - {self.categoria}"

# Cresmos la Clase Producto
class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    desc_producto = models.CharField(max_length=20)
    imagen = models.CharField(max_length=400, blank=True)
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    
    def __str__(self):
        return f"{self.id_producto} - {self.nombre_producto} ({self.id_categoria})"




#python manage.py createsuperuser
#Paso 2: Username: admin
#Paso 3: Email address: admin@example.com
#Paso 4: Agregar contraseña