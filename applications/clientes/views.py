from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse

from .functions import generador_num_registro

from .models import Cliente
from .forms import ClienteForm
     
from applications.empresa.models import Empresa
        

#verifica que nombre no se repita
@login_required(login_url='beses:login')
@permission_required('clientes.change_cliente', login_url='bases:login')
def verificar_cliente_existe(request):
    cliente = request.GET.get('razon_social')

    #Realiza la consulta en la base de datos para verificar si el cliente ya existe.
    existe = Cliente.objects.filter(razon_social=cliente).exists()   

    data = {'existe': existe}
    return JsonResponse(data)   


#verifica que rfc no se repita
@login_required(login_url='beses:login')
@permission_required('clientes.change_cliente', login_url='bases:login')
def verificar_rfc_cliente_existe(request):
    rfc = request.GET.get('rfc')

    #Realiza la consulta en la base de datos para verificar si la fecha y hora ya existe.
    existe2 = Cliente.objects.filter(rfc=rfc).exists()   

    data = {'existe2': existe2}
    return JsonResponse(data)   

        

#
class ClienteListar(LoginRequiredMixin, generic.ListView):
    model = Cliente
    permission_required = "clientes.view_cliente"
    template_name = 'clientes/listar.html'
    context_object_name = 'obj'

    #UTILIZADO PARA LOGO Y FAVICON
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['empresa'] = Empresa.objects.get()

        return context


    
#
class ClienteCrear(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Cliente
    permission_required = 'clientes.add_cliente'
    template_name = 'clientes/formulario.html'
    context_object_name = 'obj'
    form_class = ClienteForm
    success_url = reverse_lazy("clientes_app:clientes_listar")
    login_url = 'bases:login'
    success_message = ("Cliente creado correctamente")

    def form_valid(self, form):
        cod_reg = generador_num_registro()
        form.instance.cod_registro = cod_reg
        form.save()

        return super().form_valid(form)



#
class ClienteEditar(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'clientes.change_cliente'
    model = Cliente
    template_name = 'clientes/formulario.html'
    context_object_name = 'obj'
    form_class = ClienteForm
    success_url = reverse_lazy("clientes_app:clientes_listar")
    success_message = ("Cliente actualizado correctamente")
    login_url = 'bases:login'
    


#
class ClienteDetalle(LoginRequiredMixin, SuccessMessageMixin, generic.DetailView):
    model = Cliente
    permission_required = "clientes.view_cliente"
    template_name = 'clientes/cliente_detalle.html'
    context_object_name = 'obj'



#
@login_required(login_url='beses:login')
@permission_required('clientes.change_cliente', login_url='bases:login')
def cliente_eliminar(request, pk):
    if request.method == 'POST':
        cli = Cliente.objects.filter(id=pk).first()
        cli.delete()

        return HttpResponse('OK')
    



    




