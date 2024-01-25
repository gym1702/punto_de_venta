from django.urls import path

from .views import *

app_name = 'empresa_app'

urlpatterns =[
    path('empresa/listar/', EmpresaListar.as_view(), name='empresa_listar'),
    path('empresa/crear/', EmpresaCrear.as_view(), name='empresa_crear'),
    path('empresa/editar/<int:pk>/', EmpresaEditar.as_view(), name='empresa_editar'),
    path('empresa/eliminar/<pk>/', empresa_eliminar, name='empresa_eliminar'),
]
