from django import forms
from .models import Venta



class VentaForm(forms.Form):
    # LOS CAMPOS DE CODIGO Y CATIDAD_PROD SON CAMPOS QUE NO PERTENECEN A NINGUNA TABLA
    # SON CAMPOS QUE SE CREARON PARA ALMACENAR VALORES EN EL TEMPLATE
   
    codigo = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Codigo de barras',
                'class': 'form-control',
                'autofocus': 'true',
            }
        )
    )

    cantidad = forms.DecimalField(
        #min_value=1,
        widget=forms.NumberInput(
            attrs = {
                'value': '1',
                'class': 'form-control',
            }
        )
    )
    

    # def clean_cantidad(self):
    #     cantidad = self.cleaned_data['cantidad']
    #     if cantidad < 1:
    #         raise forms.ValidationError('Ingrese una cantidad mayor a cero')

    #     return cantidad
    


#
class VentaVoucherForm(forms.Form):

    metodo_pago = forms.ChoiceField(
        required=False,
        choices=Venta.metodo,
        widget=forms.Select(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    tipo_venta = forms.ChoiceField(
        required=False,
        choices=Venta.tipo,
        widget=forms.Select(
            attrs = {
                'class': 'form-control',
            }
        )
    )

