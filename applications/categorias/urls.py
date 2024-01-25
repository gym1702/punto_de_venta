from django.urls import path

from .views import *

app_name = 'categorias_app'

urlpatterns =[
    path('categoria/listar/', CategoriasListar.as_view(), name='categorias_listar'),
    path('categoria/crear/', CategoriaCrear.as_view(), name='categoria_crear'),
    path('categoria/editar/<int:pk>/', CategoriaEditar.as_view(), name='categoria_editar'),
    path('categoria/eliminar/<int:pk>/', categoria_eliminar, name='categoria_eliminar'),

    path('verificar_categoria_existe/', verificar_categoria_existe, name='verificar_categoria_existe')
]