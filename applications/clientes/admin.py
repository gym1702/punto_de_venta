from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'rfc', 'direccion', 'telefono', 'email')
    #list_filter = ['activo']
    search_fields = ['razon_social',  'rfc', 'telefono', 'email',]
    list_per_page = 10
    list_display_links = ['razon_social', 'razon_social',]


admin.site.register(Cliente, ClienteAdmin)