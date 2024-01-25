from django.contrib import admin
from .models import Producto


#
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad', 'precio_venta', 'precio_compra', 'stock', 'categoria', 
                    'proveedor', 'fecha_modificacion', 'status')
    search_fields = ['nombre','status',]
    list_per_page = 10
    list_display_links = ['nombre',]


admin.site.register(Producto, ProductoAdmin)
