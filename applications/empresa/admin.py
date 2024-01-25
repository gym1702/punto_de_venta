from django.contrib import admin
from .models import Empresa

#
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calle', 'numero', 'colonia', 'ciudad', 'estado', 'telefono', 'web')
    
    

admin.site.register(Empresa, EmpresaAdmin)