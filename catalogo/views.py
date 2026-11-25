from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ProductoForm
from .models import Producto



def registrar_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

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

    
# ==========================================
# LISTAR PRODUCTOS
# ==========================================

def producto_lista(request):

    productos = Producto.objects.all()

    return render(
        request,
        'producto_lista.html',
        {'productos': productos}
    )