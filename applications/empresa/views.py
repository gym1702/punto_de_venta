from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse

from .models import Empresa
from .forms import EmpresaForm


#Valida que no se duplique el registro
class MixinFormInvalid:

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self. request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(form.errors, status=400)
        else:
            return response
        


#****************************************
#         CLASES PARA EMPRESA
#****************************************
class EmpresaListar(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = Empresa
    permission_required = "empresa.view_empresa"
    template_name = 'empresa/listar.html'
    context_object_name = 'obj'

    #UTILIZADO PARA LOGO Y FAVICON
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['empresa'] = Empresa.objects.get()

        return context



class EmpresaCrear(LoginRequiredMixin, SuccessMessageMixin, MixinFormInvalid, generic.CreateView):
    model = Empresa
    permission_required = 'empresa.add_empresa'
    template_name = 'empresa/formulario.html'
    context_object_name = 'obj'
    form_class = EmpresaForm
    success_url = reverse_lazy("empresa_app:empresa_listar")
    login_url = 'bases:login'
    success_message = ("Empresa creada correctamente")


    # def form_valid(self, form):
    #     form.instance.usuario_crea = self.request.user
    #     form.save()
    #     return super().form_valid(form)
    

class EmpresaEditar(LoginRequiredMixin, SuccessMessageMixin, MixinFormInvalid, generic.UpdateView):
    permission_required = 'empresa.change_empresa'
    model = Empresa
    template_name = 'empresa/formulario.html'
    context_object_name = 'obj'
    form_class = EmpresaForm
    success_url = reverse_lazy("empresa_app:empresa_listar")
    success_message = ("Empresa actualizada correctamente")

#     def form_valid(self, form):
#         if form.is_valid():
#             form.instance.usuario_edita = self.request.user.full_name
#             form.save()
#         else:
#             pass    
        

#         return super().form_valid(form)
    


@login_required(login_url='beses:login')
@permission_required('empresa.change_empresa', login_url='bases:login')
def empresa_eliminar(request, pk):
    if request.method == 'POST':

        emp = Empresa.objects.filter(id=pk).first()

        emp.delete()  

        return HttpResponse('OK')