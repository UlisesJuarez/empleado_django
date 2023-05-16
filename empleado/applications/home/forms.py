from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        #fields = ('__all__')
        
        fields=(
            'titulo',
            'subtitulo',
            'cantidad',
        )

        #en widgets podemos personalizar los campo del modelo
        widgets={
            'titulo':forms.TextInput(
                #atributos del elemento html
                attrs={
                    'placeholder':'Ingresa el titulo'
                }
            )
        }


    def clean_cantidad(self):
        cantidad=self.cleaned_data["cantidad"]
        if cantidad <10:
            raise forms.ValidationError('Ingrese una cantidad mayor a 10')

        return cantidad
