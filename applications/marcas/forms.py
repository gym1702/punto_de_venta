from django import forms
from .models import Marca


class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ('nombre',)
              
           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        