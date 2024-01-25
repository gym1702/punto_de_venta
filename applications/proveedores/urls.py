from django.urls import path

from .views import * 

app_name = 'proveedores_app'

urlpatterns =[
    path('proveedores/listar/', ProveedorListar.as_view(), name='proveedores_listar'),
    path('proveedores/crear/', ProveedorCrear.as_view(), name='proveedor_crear'),
    path('proveedores/editar/<int:pk>/', ProveedorEditar.as_view(), name='proveedor_editar'),
    path('proveedores/detalle/<int:pk>/', ProveedorDetalle.as_view(), name='proveedor_detalle'),
    path('proveedores/eliminar/<int:pk>/', proveedor_eliminar, name='proveedor_eliminar'),

    path('verificar_proveedor_existe/', verificar_proveedor_existe, name='verificar_proveedor_existe'),
    path('verificar_rfc_proveedor_existe/', verificar_rfc_proveedor_existe, name='verificar_rfc_proveedor_existe'),
]