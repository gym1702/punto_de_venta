from django import forms
from .models import Empresa


#****************************************
#       FORMULARIO PARA EMPRESA 
#****************************************
class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ('nombre', 'nombre_corto', 'eslogan', 'calle', 'numero', 'colonia', 'referencia', 'ciudad', 'estado', 'pais', 'cp',
                  'telefono', 'email', 'web', 'logo_principal', 'logo_secundario',)
                
           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
