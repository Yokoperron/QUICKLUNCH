from django.db import models

# Create your models here.


from django.db import models


class Producto(models.Model):

    imagen= models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    descripcion = models.TextField(
        blank=True
    )

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    activo = models.BooleanField(
        default=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.nombre
