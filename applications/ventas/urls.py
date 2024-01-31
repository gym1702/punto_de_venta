from django.urls import path

from .views import * 

app_name = 'ventas_app'

urlpatterns =[
    path('ventas/', AgregarCarrito.as_view(), name='agregar_carrito'),
    path('ventas/actualiza_carrito/<int:pk>', ActualizaCarrito.as_view(), name='actualizar_carrito'),
    path('ventas/eliminar_carrito/<int:pk>/', EliminarItemCarrito.as_view(), name='eliminar_item_carrito'),
    path('ventas/venta_simple/', ProcesoVentaSimple.as_view(), name='venta_simple'),
    path('ventas/voucher/', ProcesoVentaVoucher.as_view(), name='venta_voucher'),
    path('ventas/venta', ProcesoVenta.as_view(), name='venta'),
    path('ventas/voucher_pdf/<pk>/', VentaVoucherPdf.as_view(), name='venta_voucher_pdf'),
    path('ventas/limpiar_carrito/', CarritoLimpiar.as_view(), name='limpiar_carrito'),
    path('ventas/ultimas_ventas/', UltimasVentas.as_view(), name='ultimas_ventas'),
    path('ventas/anular/<int:pk>/', venta_anular, name='venta_anular'),
    #path('ventas-id/<int:pk>/', id_venta, name='venta_id'),
    path('ventas/<int:pk>/', VentasDetalle.as_view(), name='ventas_detalle'),

    
    # path('verificar_producto_existe/', verificar_producto_existe, name='verificar_producto_existe'),
    # path('verificar_codigo_producto_existe/', verificar_codigo_producto_existe, name='verificar_codigo_producto_existe'),
]