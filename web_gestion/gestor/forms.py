from django import forms
from .models import *

class Producto_Form(forms.ModelForm):
    class Meta:
        model = Productos_li
        fields = ('nombre', 'stock', 'fecha_vencimiento', 'lote', 'punto_de_pedido')

UNIDAD_CHOICES = (
    ('Lts', 'Lts'),
    ('mls', 'mls'),
    ('g', 'g'),
    ('kg', 'kg'),
    ('unidad', 'unidad'),
)

class Insumo_Form(forms.ModelForm):

    unidad = forms.ChoiceField(choices=UNIDAD_CHOICES)

    class Meta:
        model = Insumos_li
        fields = ('nombre', 'stock', 'unidad', 'fecha_vencimiento', 'lote', 'punto_de_pedido')

class Envase_Form(forms.ModelForm):
    class Meta:
        model = Envases_li
        fields = ('nombre', 'stock', 'punto_de_pedido')