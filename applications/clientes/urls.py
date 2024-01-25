from django.urls import path

from .views import * 

app_name = 'clientes_app'

urlpatterns =[
    path('clientes/listar/', ClienteListar.as_view(), name='clientes_listar'),
    path('clientes/crear/', ClienteCrear.as_view(), name='cliente_crear'),
    path('clientes/editar/<int:pk>/', ClienteEditar.as_view(), name='cliente_editar'),
    path('clientes/detalle/<int:pk>/', ClienteDetalle.as_view(), name='cliente_detalle'),
    path('clientes/eliminar/<int:pk>/', cliente_eliminar, name='cliente_eliminar'),

    path('verificar_cliente_existe/', verificar_cliente_existe, name='verificar_cliente_existe'),
    path('verificar_rfc_cliente_existe/', verificar_rfc_cliente_existe, name='verificar_rfc_cliente_existe'),
]