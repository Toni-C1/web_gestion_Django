from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    insumos = Insumo.objects.all()
    return render(request, "gestor/home.html", {"productos":productos, "insumos":insumos})

def productos(request):
    productos = Producto.objects.all()
    return render(request, "gestor/productos.html", {"productos":productos})

def insumos(request):
    insumos = Insumo.objects.all()
    return render(request, "gestor/insumos.html", {"insumos":insumos})

