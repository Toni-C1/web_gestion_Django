from django import forms
from .models import *

class Producto_Form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('nombre', 'stock')

class Insumo_Form(forms.ModelForm):
    class Meta:
        model = Insumos
        fields = ('nombre', 'stock')