from django.contrib import admin
from .models import Producto #Descuento


#
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad', 'precio_venta', 'precio_compra', 'stock', 'categoria', 
                    'proveedor', 'fecha_modificacion', 'descuento', 'fecha_inicio_descuento', 
                    'fecha_fin_descuento', 'status')
    search_fields = ['nombre','status',]
    list_per_page = 10
    list_display_links = ['nombre',]



# class DescuentoAdmin(admin.ModelAdmin):
#     list_display = ('producto', 'descuento', 'fecha_inicio', 'fecha_fin',)
#     list_per_page = 10



admin.site.register(Producto, ProductoAdmin)
#admin.site.register(Descuento, DescuentoAdmin)