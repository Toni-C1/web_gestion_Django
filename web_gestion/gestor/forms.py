from django import forms
from .models import *

class Producto_Form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'stock')

class Insumo_Form(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ('nombre', 'stock')