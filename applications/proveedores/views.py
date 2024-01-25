from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse

#from .functions import generador_num_registro

from .models import Proveedor
from .forms import ProveedorForm
     
from applications.empresa.models import Empresa
        

#verifica que nombre no se repita
@login_required(login_url='beses:login')
@permission_required('proveedores.change_proveedor', login_url='bases:login')
def verificar_proveedor_existe(request):
    proveedor = request.GET.get('razon_social')

    #Realiza la consulta en la base de datos para verificar si el proveedor ya existe.
    existe = Proveedor.objects.filter(razon_social=proveedor).exists()   

    data = {'existe': existe}
    return JsonResponse(data)   


#verifica que rfc no se repita
@login_required(login_url='beses:login')
@permission_required('proveedores.change_proveedor', login_url='bases:login')
def verificar_rfc_proveedor_existe(request):
    rfc = request.GET.get('rfc')

    #Realiza la consulta en la base de datos para verificar si la fecha y hora ya existe.
    existe2 = Proveedor.objects.filter(rfc=rfc).exists()   

    data = {'existe2': existe2}
    return JsonResponse(data)   

        

#
class ProveedorListar(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    permission_required = "proveedores.view_proveedor"
    template_name = 'proveedores/listar.html'
    context_object_name = 'obj'

    #UTILIZADO PARA LOGO Y FAVICON
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['empresa'] = Empresa.objects.get()

        return context


    
#
class ProveedorCrear(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Proveedor
    permission_required = 'proveedores.add_proveedor'
    template_name = 'proveedores/formulario.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy("proveedores_app:proveedores_listar")
    login_url = 'bases:login'
    success_message = ("Proveedor creado correctamente")



#
class ProveedorEditar(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'proveedores.change_proveedor'
    model = Proveedor
    template_name = 'proveedores/formulario.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy("proveedores_app:proveedores_listar")
    success_message = ("Proveedor actualizado correctamente")
    login_url = 'bases:login'
    


#
class ProveedorDetalle(LoginRequiredMixin, SuccessMessageMixin, generic.DetailView):
    model = Proveedor
    permission_required = "proveedores.view_proveedor"
    template_name = 'proveedores/proveedor_detalle.html'
    context_object_name = 'obj'



#
@login_required(login_url='beses:login')
@permission_required('proveedores.change_proveedor', login_url='bases:login')
def proveedor_eliminar(request, pk):
    if request.method == 'POST':
        prov = Proveedor.objects.filter(id=pk).first()
        prov.delete()

        return HttpResponse('OK')
    

    
    



    




