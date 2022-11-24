#Los modelos son clases que nos permiten definir la estructura de los datos
#para la base de datos de django
#Django automáticamente los mapeará a objetos

from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Últa modificación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
