from django import forms
from .models import Cliente



class ClienteForm(forms.ModelForm):

    # fecha_nac = forms.DateInput()

    class Meta:
        model = Cliente
        fields = ('id', 'razon_social', 'rfc', 'calle_no', 'ciudad', 'colonia', 
                  'estado', 'cp', 'telefono', 'email', 'activo', 'credito')
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        #self.fields['edad'].widget.attrs['readonly'] = True


    