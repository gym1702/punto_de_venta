from typing import Any
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse

from .models import Producto
from .forms import ProductoForm

from applications.empresa.models import Empresa

from applications.ventas.models import VentaDetalle

from .utils import render_to_pdf

     
        

#verifica que nombre no se repita
@login_required(login_url='beses:login')
@permission_required('productos.change_producto', login_url='bases:login')
def verificar_producto_existe(request):
    producto = request.GET.get('nombre')

    #Realiza la consulta en la base de datos para verificar si la fecha y hora ya existe.
    existe = Producto.objects.filter(nombre=producto).exists()   

    data = {'existe': existe}
    return JsonResponse(data)   


#verifica que nombre no se repita
@login_required(login_url='beses:login')
@permission_required('productos.change_producto', login_url='bases:login')
def verificar_codigo_producto_existe(request):
    codigo = request.GET.get('codigo')

    #Realiza la consulta en la base de datos para verificar si la fecha y hora ya existe.
    existe2 = Producto.objects.filter(codigo=codigo).exists()   

    data = {'existe2': existe2}
    return JsonResponse(data)   

        

#
class ProductoListar(LoginRequiredMixin, generic.ListView):
    model = Producto
    permission_required = "productos.view_producto"
    template_name = 'productos/listar.html'
    context_object_name = 'obj'

     #UTILIZADO PARA LOGO Y FAVICON
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['empresa'] = Empresa.objects.get()

        return context


    
#
class ProductoCrear(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Producto
    permission_required = 'productos.add_producto'
    template_name = 'productos/formulario.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("productos_app:productos_listar")
    login_url = 'bases:login'
    success_message = ("Producto creado correctamente")



#
class ProductoEditar(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'productos.change_producto'
    model = Producto
    template_name = 'productos/formulario.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("productos_app:productos_listar")
    success_message = ("Producto actualizado correctamente")
    login_url = 'bases:login'
    


#
class ProductoDetalle(LoginRequiredMixin, SuccessMessageMixin, generic.DetailView):
    model = Producto
    permission_required = "productos.view_producto"
    template_name = 'productos/producto_detalle.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)

        context["ventas_mes"] = VentaDetalle.objects.ventas_mes_producto(
            self.kwargs['pk']
        )

        return context



#
@login_required(login_url='beses:login')
@permission_required('productos.change_producto', login_url='bases:login')
def producto_eliminar(request, pk):
    if request.method == 'POST':
        prod = Producto.objects.filter(id=pk).first()
        prod.delete()

        return HttpResponse('OK')
    


#IMRIMIR DETALLE EN PDF
class ProductDetailViewPdf(LoginRequiredMixin, generic.View):
    
    def get(self, request, *args, **kwargs):
        producto = Producto.objects.get(id=self.kwargs['pk'])
        data = {
            'product': producto,
            'ventas_mes': VentaDetalle.objects.ventas_mes_producto(self.kwargs['pk'])
        }
        pdf = render_to_pdf('productos/imprimir_detalle.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    



#####ESTO POR VERSE
#
# class FiltrosProductoListView(LoginRequiredMixin, generic.ListView):
#     template_name = "productos/reportes.html"
#     context_object_name = 'productos'

#     def get_queryset(self):

#         queryset = Producto.objects.filter(
#             kword=self.request.GET.get("kword", ''),
#             date_start=self.request.GET.get("date_start", ''),
#             date_end=self.request.GET.get("date_end", ''),
#             provider=self.request.GET.get("proveedor", ''),
#             marca=self.request.GET.get("marca", ''),
#             order=self.request.GET.get("orden", ''),
#         )
#         return queryset
    



    




