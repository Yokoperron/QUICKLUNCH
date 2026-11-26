
from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'nombre',
            'descripcion',
            'precio',
            'imagen'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripcion del producto'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio del producto',
                'min': '0',
                'step': '0'
            }),

            
        }
    def clean_precio(self):
        precio = self.cleaned_data['precio']

        if precio < 0:
            raise forms.ValidationError(
                'El precio no puede ser negativo.'
            )

        return precio