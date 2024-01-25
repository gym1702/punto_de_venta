from typing import Any
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse

from .models import Categoria
from .forms import CategoriaForm
from applications.empresa.models import Empresa


#
class CategoriasListar(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'categorias/listar.html'
    permission_required = "categorias.view_categoria"
    context_object_name = 'obj'


    #UTILIZADO PARA LOGO Y FAVICON
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['empresa'] = Empresa.objects.get()

        return context
    

#
class CategoriaCrear(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Categoria
    permission_required = 'categorias.add_categoria'
    template_name = 'categorias/formulario.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias_app:categorias_listar')
    login_url = 'base:login'
    success_message = ('Categoria creada exitosamente')


#
class CategoriaEditar(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Categoria
    permission_required = 'categorias.change_categoria'
    template_name = 'categorias/formulario.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias_app:categorias_listar')
    login_url = 'base:login'
    success_message = ('Categoria actualizada exitosamente')


#
@login_required(login_url='base:login')
@permission_required('categorias.change_categoria',login_url='base:login')
def categoria_eliminar(request, pk):
    if request.method == 'POST':
        cat = Categoria.objects.filter(pk=pk).first()
        cat.delete()

        return HttpResponse('OK')



#verifica que nombre no se repita
@login_required(login_url='beses:login')
@permission_required('categorias.change_categoria', login_url='bases:login')
def verificar_categoria_existe(request):
    nombre = request.GET.get('nombre')

    #Realiza la consulta en la base de datos para verificar si el nombre ya existe.
    existe = Categoria.objects.filter(nombre=nombre).exists() 

    data = {'existe': existe}
    return JsonResponse(data)  


