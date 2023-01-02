from django import forms
from .models import *

class Producto_Form(forms.ModelForm):
    class Meta:
        model = Productos_l
        fields = ('nombre', 'stock', 'fecha_vencimiento', 'lote')

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
        model = Insumos_l
        fields = ('nombre', 'stock', 'unidad', 'fecha_vencimiento', 'lote')

class Envase_Form(forms.ModelForm):
    class Meta:
        model = Envases
        fields = ('nombre', 'stock')