"""
URL configuration for QUICKLUNCH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalogo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #catalogo de productos
    path('', producto_lista, name='producto_lista'),

    #registrar productos
    path('producto/registrar/', registrar_producto, name='registrar_producto'),

    #actualizar producto
    path('producto/editar/<int:id>/', editar_producto, name='editar_producto'),

    #deshabilitar producto
    path('producto/deshabilitar_producto/<int:id>/', deshabilitar_producto, name='deshabilitar_producto'),

    #habilitar producto
    path('producto/habilitar/<int:id>/', habilitar_producto, name='habilitar_producto'),
    


]

# Configuración para visualizar imágenes durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
