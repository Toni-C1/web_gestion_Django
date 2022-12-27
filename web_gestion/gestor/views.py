from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    insumos = Insumo.objects.all()
    return render(request, "gestor/home.html", {"productos":productos, "insumos":insumos})

def productos(request):
    productos = Producto.objects.all()
    
    #####################################

    #Formulario cargar nuevo producto a la bd
    form = Producto_Form()
    if request.method == "POST":
    
        form = Producto_Form(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    else:
        form = Producto_Form()
    ####################################

    context = {
        'form': form,
        'productos': productos
        }

    return render(request, "gestor/productos.html", context)


def insumos(request):
    insumos = Insumo.objects.all()

    #####################################

    #Formulario cargar nuevo insumo a la bd
    form = Insumo_Form()
    if request.method == "POST":
    
        form = Insumo_Form(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    else:
        form = Insumo_Form()
    ####################################

    context = {
        'form': form,
        'insumos': insumos
        }
    return render(request, "gestor/insumos.html", context)

