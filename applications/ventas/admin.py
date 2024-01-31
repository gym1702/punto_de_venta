from django.contrib import admin
from .models import Venta, VentaDetalle, Carrito

class VentaDetalleInline(admin.TabularInline):
    model = VentaDetalle
    readonly_fields = ('venta', 'producto', 'cantidad', 'precio_venta', 'iva', 'anulada',)
    extra = 0


class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'cantidad', 'monto', 'tipo_venta', 'metodo_pago', 'venta_cerrada', 'venta_anulada', 'usuario',]
    list_filter = ['venta_cerrada', 'venta_anulada',]
    search_fields = ['id', 'tipo_venta', 'tipo_pago', 'monto',]
    list_per_page = 20
    inlines = [VentaDetalleInline]



class CarritoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'producto', 'cantidad', 'fecha',]
    search_fields = ['codigo', 'producto',]
    list_per_page = 20



# Register your models here.
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(VentaDetalle)
