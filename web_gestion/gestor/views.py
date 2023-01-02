from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "gestor/index.html")

def home(request):
    return render(request, "gestor/home.html")

def productos_crear(request):
    productos = Productos_li.objects.all()
    
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

    return render(request, "gestor/productos_crear.html", context)

def productos_editar(request, id_i):

    id_i = int(id_i)

    try:
        producto_sel = Productos_li.objects.get(id=id_i)
    except Productos_li.DoesNotExist:
        return redirect('/productos_crear')
 
    

    form_e = Producto_Form(request.POST or None,  instance=producto_sel)

    
 
    if form_e.is_valid():
        form_e.save()
        return redirect("/productos_crear")


    productos = Productos_li.objects.all()

    context = {
        'form_e': form_e,
        'productos': productos,
        'producto_sel': producto_sel,
        }
    return render(request, "gestor/productos_editar.html", context)

def productos_eliminar(request, id_i):
    
    id_productos = Productos_li.objects.get(id=id_i)
    
    id_productos.delete()
    
    return redirect("/productos_crear")

def insumos_crear(request):
    insumos = Insumos_li.objects.all()
    envases = Envases_li.objects.all()

    #####################################
    #Formulario para cargar nuevo insumo a la bd
    form_c = Insumo_Form()
    if request.method == "POST":
    
        form_c = Insumo_Form(request.POST)

        if form_c.is_valid():
            post = form_c.save(commit=False)
            post.save()

    else:
        form_c = Insumo_Form()
    ####################################

    context = {
        'form_c': form_c,
        'insumos': insumos,
        'envases': envases,
        }
    return render(request, "gestor/insumos_crear.html", context)

def insumos_editar(request, id_i):

    id_i = int(id_i)

    try:
        insumo_sel = Insumos_li.objects.get(id=id_i)
    except Insumos_li.DoesNotExist:
        return redirect('/insumos_crear')
 
    

    form_e = Insumo_Form(request.POST or None,  instance=insumo_sel)

    
 
    if form_e.is_valid():
        form_e.save()
        return redirect("/insumos_crear")


    insumos = Insumos_li.objects.all()
    envases = Envases_li.objects.all()

    context = {
        'form_e': form_e,
        'insumos': insumos,
        'insumo_sel': insumo_sel,
        'envases': envases,
        }
    return render(request, "gestor/insumos_editar.html", context)

def insumos_eliminar(request, id_i):
    
    id_insumos = Insumos_li.objects.get(id=id_i)
    
    id_insumos.delete()
    
    return redirect("/insumos_crear")
  
def envases_crear(request):
    insumos = Insumos_li.objects.all()
    envases = Envases_li.objects.all()

    #####################################
    #Formulario para cargar nuevo insumo a la bd
    form_c = Envase_Form()
    if request.method == "POST":
    
        form_c = Envase_Form(request.POST)

        if form_c.is_valid():
            post = form_c.save(commit=False)
            post.save()

    else:
        form_c = Envase_Form()
    ####################################

    context = {
        'form_c': form_c,
        'insumos': insumos,
        'envases': envases,
        }
    return render(request, "gestor/envases_crear.html", context)

def envases_editar(request, id_i):

    id_i = int(id_i)

    try:
        envase_sel = Envases_li.objects.get(id=id_i)
    except Envases_li.DoesNotExist:
        return redirect('/envases_crear')
 
    

    form_e = Envase_Form(request.POST or None,  instance=envase_sel)

    
 
    if form_e.is_valid():
        form_e.save()
        return redirect("/envases_crear")


    insumos = Insumos_li.objects.all()
    envases = Envases_li.objects.all()

    context = {
        'form_e': form_e,
        'insumos': insumos,
        'insumo_sel': envase_sel,
        'envases': envases,
        }
    return render(request, "gestor/insumos_editar.html", context)

def envases_eliminar(request, id_i):
    
    id_envases = Envases_li.objects.get(id=id_i)
    
    id_envases.delete()
    
    return redirect("/envases_crear")