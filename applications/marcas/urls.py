from django.urls import path

from .views import *

app_name = 'marcas_app'

urlpatterns = [
    path('marca/listar/', MarcasListar.as_view(), name='marcas_listar'),
    path('marca/crear/', MarcaCrear.as_view(), name='marca_crear'),
    path('marca/editar/<int:pk>/', MarcaEditar.as_view(), name='marca_editar'),
    path('marca/eliminar/<int:pk>/', marca_eliminar, name='marca_eliminar'),

    path('verificar_marca_existe/', verificar_marca_existe, name='verificar_marca_existe')

]