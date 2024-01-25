from django.urls import path

from .views import * 

app_name = 'productos_app'

urlpatterns =[
    path('productos/listar/', ProductoListar.as_view(), name='productos_listar'),
    path('productos/crear/', ProductoCrear.as_view(), name='producto_crear'),
    path('productos/editar/<int:pk>/', ProductoEditar.as_view(), name='producto_editar'),
    path('productos/detalle/<int:pk>/', ProductoDetalle.as_view(), name='producto_detalle'),
    path('productos/eliminar/<int:pk>/', producto_eliminar, name='producto_eliminar'),

    path('verificar_producto_existe/', verificar_producto_existe, name='verificar_producto_existe'),
    path('verificar_codigo_producto_existe/', verificar_codigo_producto_existe, name='verificar_codigo_producto_existe'),

    #path('producto/detalle/print/<int:pk>/', ProductDetailViewPdf.as_view(), name='producto_detalle_print'),
]
