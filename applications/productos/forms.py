from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'codigo', 'descripcion', 'precio_compra', 'unidad',
                  'precio_venta', 'imagenes', 'stock', 'categoria', 'marca', 'proveedor', 
                  'fecha_vencimiento', 'status', 'descuento', 'fecha_inicio_descuento', 
                    'fecha_fin_descuento',)

        widgets = {
            'descripcion': forms.Textarea(attrs={'rows':4}),
        }
                
           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        # self.fields['edad'].widget.attrs['readonly'] = True


class BusquedaProductoForm(forms.Form):
    codigo = forms.CharField(label='Código', max_length=100)

    


    
    
    