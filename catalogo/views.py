from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST

from .forms import ProductoForm
from .models import Producto


#REGISTRAR PRODUCTOS

@staff_member_required
def registrar_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Producto registrado correctamente.'
            )

            return redirect('producto_lista')

    else:
        formulario = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'formulario': formulario}
    )


# LISTA DE PRODUCTOS

def producto_lista(request):

    busqueda = request.GET.get('buscar', '')

    if request.user.is_staff:

        productos = Producto.objects.all()

    else:

        productos = Producto.objects.filter(activo=True)

    # FILTRO DE BÚSQUEDA
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    # SEPARAR PRODUCTOS HABILITADOS Y DESHABILITADOS
    productos_activos = productos.filter(activo=True)

    productos_inactivos = productos.filter(activo=False)

    return render(
        request,
        'producto_lista.html',
        {
            'productos_activos': productos_activos,
            'productos_inactivos': productos_inactivos,
            'busqueda': busqueda
        }
    )

    

    return render(request, 'producto_lista.html',{'productos_activos': productos_activos, 'productos_inactivos': productos_inactivos, 'busqueda':busqueda})

# EDITAR PRODUCTO

@staff_member_required
def editar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Producto actualizado correctamente.'
            )

            return redirect('producto_lista')

    else:
        formulario = ProductoForm(instance=producto)

    return render(
        request,
        'producto_form.html',
        {'formulario': formulario, 'producto': producto}
    )

# DESHABILITAR PRODUCTO
@staff_member_required
@require_POST
def deshabilitar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    producto.activo = False
    producto.save()

    messages.success(
        request,
        'Producto deshabilitado correctamente.'
    )

    return redirect('producto_lista')


# HABILITAR PRODUCTO
@staff_member_required
@require_POST
def habilitar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    producto.activo = True
    producto.save()

    messages.success(
        request,
        'Producto habilitado correctamente.'
    )

    return redirect('producto_lista')