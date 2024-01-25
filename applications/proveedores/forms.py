from django import forms
from .models import Proveedor



class ProveedorForm(forms.ModelForm):

    # fecha_nac = forms.DateInput()

    class Meta:
        model = Proveedor
        fields = ('razon_social', 'rfc', 'calle_no', 'ciudad', 'colonia', 'web',
                  'estado', 'cp', 'telefono', 'email', 'activo', 'credito', 'que_vende')
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        #self.fields['edad'].widget.attrs['readonly'] = True


    