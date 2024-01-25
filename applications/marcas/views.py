from typing import Any
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse

from .models import Marca
from .forms import MarcaForm
from applications.empresa.models import Empresa


#
class MarcasListar(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = 'marcas/listar.html'
    permission_required = "marcas.view_marca"
    context_object_name = 'obj'


    #UTILIZADO PARA LOGO Y FAVICON
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['empresa'] = Empresa.objects.get()

        return context
    

#
class MarcaCrear(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Marca
    permission_required = 'marcas.add_marca'
    template_name = 'marcas/formulario.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('marcas_app:marcas_listar')
    login_url = 'base:login'
    success_message = ('Marca creada exitosamente')


#
class MarcaEditar(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Marca
    permission_required = 'marcas.change_marca'
    template_name = 'marcas/formulario.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('marcas_app:marcas_listar')
    login_url = 'base:login'
    success_message = ('Marca actualizada exitosamente')


#
@login_required(login_url='base:login')
@permission_required('marcas.change_marca',login_url='base:login')
def marca_eliminar(request, pk):
    if request.method == 'POST':
        marca = Marca.objects.filter(pk=pk).first()
        marca.delete()

        return HttpResponse('OK')



#verifica que nombre no se repita
@login_required(login_url='beses:login')
@permission_required('marcas.change_marca', login_url='bases:login')
def verificar_marca_existe(request):
    nombre = request.GET.get('nombre')

    #Realiza la consulta en la base de datos para verificar si el nombre ya existe.
    existe = Marca.objects.filter(nombre=nombre).exists() 

    data = {'existe': existe}
    return JsonResponse(data)  
