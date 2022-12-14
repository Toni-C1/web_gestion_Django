#Los modelos son clases que nos permiten definir la estructura de los datos
#para la base de datos de django
#Django automáticamente los mapeará a objetos
#pipenv run python manage.py makemigrations
#pipenv run python manage.py migrate

from django.db import models

# Create your models here.


class Productos_li(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    punto_de_pedido = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    lote = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Insumos_li(models.Model):    
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    unidad = models.CharField(max_length=100)
    punto_de_pedido = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    lote = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Últa modificación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"


class Envases_li(models.Model):    
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    punto_de_pedido = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Últa modificación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Envase"
        verbose_name_plural = "Envases"

class Pedidos_productos_li(models.Model):    
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    cliente = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Últa modificación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class Lista_compras_li(models.Model):    
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    insumo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Últa modificación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

