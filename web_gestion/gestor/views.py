from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def index(request):

    ##chekeo de pedidos pendientes
    pedidos = Pedidos_productos_li.objects.all()
    pendientes = []

    for pedido in pedidos:
        if pedido.estado == 'Pendiente':
            pendientes.append(pedido)
    
    cantidad_pendientes = len(pendientes)

    ##chekeo de Productos por debajo de punto de pedido##
    productos = Productos_li.objects.all()

    pocos_productos = []

    for producto in productos:
        if producto.stock <= producto.punto_de_pedido:
            pocos_productos.append(producto)

    ##chekeo de Insumos por debajo de punto de pedido##
    insumos = Insumos_li.objects.all()
    

    pocos_insumos = []

    for insumo in insumos:
        if insumo.stock <= insumo.punto_de_pedido:
            pocos_insumos.append(insumo)
    
    ##chekeo de Envases por debajo de punto de pedido##
    envases = Envases_li.objects.all()
    pocos_envases = []
    
    for envase in envases:
        if insumo.stock <= insumo.punto_de_pedido:
            pocos_envases.append(envase)

    context = {
        'pocos_productos': pocos_productos,
        'pocos_insumos': pocos_insumos,
        'pocos_envases': pocos_envases,
        'pendientes': pendientes,
        'cantidad_pendientes': cantidad_pendientes,
        }

    return render(request, "gestor/index.html", context)

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

def gestion_pedidos(request):

    context = {
        
        }
    return render(request, "gestor/gestion_pedidos.html", context)

def pedido_eliminar(request, id_i):
    
    pedido = Pedidos_productos_li.objects.get(id=id_i)
    
    pedido.delete()
    
    return redirect("/gestion_pedidos")

def historial_pedidos(request):

    pedidos = Pedidos_productos_li.objects.all()

    context = {
        'pedidos': pedidos,
        }
    return render(request, "gestor/historial_pedidos.html", context)

def carga_pedidos(request):

    #####################################

    #Formulario cargar nuevo pedido -> selecciono cliente
    form = Pedido_Form(initial={'estado':'Pendiente'})
    if request.method == "POST":
    
        form = Pedido_Form(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            u = Pedidos_productos_li.objects.last()
            url_prox = "/carga_pedidos_2/"+ str(u.id)
            #print(f"\nurl_prox:{url_prox}")
            
            return redirect(url_prox)

    else:
        print("Formulario no válido")
        form = Pedido_Form()
    ####################################

    context = {
        'form': form,
        }

    return render(request, "gestor/carga_pedidos.html", context)

def carga_pedidos_2(request, id_i):

    id_u = int(id_i)

    ultimo = Pedidos_productos_li.objects.get(id=id_u)
    #####################################

    #Formulario cargar productos al pedido
  
    form = Prod_en_pedido_Form(request.POST)

    if form.is_valid():
        post = form.save(commit=False)

        post.save()
        
    #return redirect("/gestion_pedidos")

    else:
        form = Prod_en_pedido_Form()
    ####################################

    

    lista_actual = []
 
    
    try:
        lista_actual = Pedido_intermedio_li.objects.values().filter(id_pedido=ultimo.id)
        
        for producto in lista_actual:
        
            prod = Productos_li.objects.get(id=producto['producto_id'])
            producto['producto_id'] = prod

    except Pedido_intermedio_li.DoesNotExist:
        return redirect('/carga_pedidos_2')
    
    
    


    context = {
        'form': form,
        'lista_actual': lista_actual,
        'ultimo': ultimo,
        #'pedido_actual': pedido_actual,
        }

    return render(request, "gestor/carga_pedidos_2.html", context)

def modificar_pedidos(request):

    pedidos = Pedidos_productos_li.objects.all()

    context = {
        'pedidos': pedidos,
        }

    return render(request, "gestor/modificar_pedidos.html", context)

def clientes_crear(request):
    clientes = Clientes_li.objects.all()
    
    #####################################

    #Formulario cargar nuevo cliente a la bd
    form = Cliente_Form()
    if request.method == "POST":
    
        form = Cliente_Form(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    else:
        form = Cliente_Form()
    ####################################

    context = {
        'form': form,
        'clientes': clientes
        }

    return render(request, "gestor/clientes_crear.html", context)

def detalle_pedidos(request, id_i):

    id_i = int(id_i)

    detallar = Pedidos_productos_li.objects.get(id=id_i)

    lista_actual = []

    try:
        lista_actual = Pedido_intermedio_li.objects.values().filter(id_pedido=detallar.id)
    
        for producto in lista_actual:
        
            prod = Productos_li.objects.get(id=producto['producto_id'])
            producto['producto_id'] = prod
    
    except Pedido_intermedio_li.DoesNotExist:
        return redirect('/carga_pedidos_2')
    
    context = {
        'detallar':detallar,
        'lista_actual':lista_actual
        }

    return render(request, "gestor/detalle_pedidos.html", context)

def editar_pedidos(request, id_i):

    id_producto_en_pedido = int(id_i)

    print(f"\nid recibido: {id_producto_en_pedido}")

    produc = Pedido_intermedio_li.objects.values().filter(id=id_producto_en_pedido)

    id_2= produc[0]['id_pedido_id']
    #cliente = 

    print(f"\nid pedido: {id_2}")

    

    print(f"\nproducto: {produc}")

    

    lista_actual = []

    try:
        n_pedido = Pedido_intermedio_li.objects.get(id=id_producto_en_pedido)
        print(f"\npedido: {n_pedido}")

    except Pedido_intermedio_li.DoesNotExist:
        print(f"\nProducto no encontrado")
 
    

    form_e = Prod_en_pedido_Form(request.POST or None,  instance=n_pedido)

    
 
    if form_e.is_valid():
        form_e.save()

        #u = Pedidos_productos_li.objects.last()
        url_prox = "/carga_pedidos_2/"+ str(id_2)

        return redirect(url_prox)
    
    context = {
        'form_e':form_e,
        'n_pedido':id_2,
        'lista_actual':lista_actual
        }

    return render(request, "gestor/editar_pedidos.html", context)

def pedido_cancelado(request, id_i):
    
    id_pedido = Pedidos_productos_li.objects.get(id=id_i)
    
    id_pedido.estado = "Cancelado"

    id_pedido.save()
    
    return redirect("/modificar_pedidos")

def pedido_completado(request, id_i):
    
    id_pedido = Pedidos_productos_li.objects.get(id=id_i)
    
    id_pedido.estado = "Completado"
    id_pedido.entregado = True
    id_pedido.pagado = True


    id_pedido.save()
    
    return redirect("/modificar_pedidos")

def pedido_entregado(request, id_i):
    
    id_pedido = Pedidos_productos_li.objects.get(id=id_i)
    
    if id_pedido.entregado == False:
        id_pedido.entregado = True
    else:
        id_pedido.entregado = False

    id_pedido.save()
    
    return redirect("/modificar_pedidos")

def pedido_pagado(request, id_i):
    
    id_pedido = Pedidos_productos_li.objects.get(id=id_i)

    if id_pedido.pagado == False:
        id_pedido.pagado = True
    else:
        id_pedido.pagado = False
    

    id_pedido.save()
    
    return redirect("/modificar_pedidos")

def eliminar_de_pedido(request, id_i, id_u):
    
    id_producto = Pedido_intermedio_li.objects.get(id=id_i)
    
    id_producto.delete()

    url_prox = "/carga_pedidos_2/"+ str(id_u)
    
    return redirect(url_prox)