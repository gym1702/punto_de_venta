from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'rfc', 'direccion', 'telefono', 'email')
    list_display_links = ('id', 'razon_social',)
    search_fields = ['razon_social',  'rfc', 'telefono', 'email',]
    list_per_page = 10
    list_display_links = ['razon_social', 'razon_social',]


admin.site.register(Proveedor, ProveedorAdmin)