from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from datetime import date, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import sweetify
from sweetify.views import SweetifySuccessMixin

from applications.ventas.models import Carrito, Venta, VentaDetalle
from applications.productos.models import Producto
from .forms import VentaForm, VentaVoucherForm
from applications.empresa.models import Empresa
from .functions import procesar_venta

from .utils import render_to_pdf

import datetime
import os
from django.conf import settings


#Para emitir un sonido al cargar producto al carrito
import pygame
pygame.mixer.init()
sonido = pygame.mixer.Sound('media/sonidos/beep.wav')
# Obtén la ruta del directorio actual del proyecto
# base_dir = os.path.dirname(os.path.abspath(__file__))
# # Construye la ruta completa al archivo de sonido
# ruta_sonido = os.path.join(base_dir, 'media', 'sonidos', 'beep.wav')
# pygame.mixer.init()
# sonido = pygame.mixer.Sound(ruta_sonido)


#
class AgregarCarrito(LoginRequiredMixin, generic.FormView):
    template_name = 'ventas/ventas.html'
    form_class = VentaForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["productos"] = Carrito.objects.all().order_by('id') #El Carrito.objents viene del def form_valid
        context["total_cobrar"] = Carrito.objects.total_cobrar()
        #context["vigencia"] = Carrito.objects.vigencia()
                
        # formulario para venta con voucher
        context['form_voucher'] = VentaVoucherForm

        #Muestra fecha
        context["fecha"] = datetime.datetime.now()

        #UTILIZADO PARA LOGO Y FAVICON
        context['empresa'] = Empresa.objects.get()

        return context
    
    
    def form_valid(self, form):

        codigo = form.cleaned_data['codigo']
        cantidad = form.cleaned_data['cantidad']

        try:
            producto = Producto.objects.get(codigo=codigo)

            #Verifica fecha para asignar descuento si no esta vigente modifica descuento a 0
            fecha_actual = timezone.now().date()  
            fecha = fecha_actual - timedelta(days=1)
            fecha_fin = Producto.objects.filter(codigo=codigo, fecha_fin_descuento__lte=fecha)

            if fecha_fin.exists():
                producto.descuento = 0
                producto.save()
            #
            
            obj, existe = Carrito.objects.get_or_create(
                codigo = codigo,            
                defaults = {
                    'producto': producto,
                    'cantidad': cantidad,
                }
            )
            # Reproducir sonido
            sonido.play()
           

            if not existe:
                obj.cantidad = obj.cantidad + cantidad
                obj.save()
                # Reproducir sonido
                sonido.play()

            
        except ObjectDoesNotExist:
            messages.error(self.request, f'Producto con código {codigo} no encontrado.')
            #sweetify.error(self.request, '¡Error!', text='Producto con código no encontrado.', persistent='Ok')


        return super(AgregarCarrito, self).form_valid(form)



#
class ActualizaCarrito(LoginRequiredMixin, generic.View):
    """ quita en 1 la cantidad en un carshop """

    def post(self, request, *args, **kwargs):
        car = Carrito.objects.get(id=self.kwargs['pk'])
        if car.cantidad > 1:
            car.cantidad = car.cantidad - 1
            car.save()
        else:
            car.delete()

        return HttpResponseRedirect(reverse('ventas_app:agregar_carrito'))



#
class EliminarItemCarrito(LoginRequiredMixin, generic.DeleteView):
    model = Carrito
    success_url = reverse_lazy('ventas_app:agregar_carrito')



#
class CarritoLimpiar(LoginRequiredMixin, generic.View):
    
    def post(self, request, *args, **kwargs):
        
        Carrito.objects.all().delete()
        
        return HttpResponseRedirect(reverse('ventas_app:agregar_carrito'))



#
class ProcesoVentaSimple(LoginRequiredMixin, generic.View):
    """ Procesa una venta simple sin comprobante"""
    # Ver archivo functions que contiene la funcion con el proceso

    def post(self, request, *args, **kwargs):
        
        procesar_venta(
            self = self,
            tipo_venta = 'Sin comprobante',
            metodo_pago = 'Efectivo',
            usuario = self.request.user,
        )
        
        return HttpResponseRedirect(reverse('ventas_app:agregar_carrito'))
    


#
class ProcesoVentaVoucher(LoginRequiredMixin, generic.FormView):
    form_class = VentaVoucherForm
    success_url = '.'
    
    def form_valid(self, form):
        tipo_venta = form.cleaned_data['tipo_venta']
        metodo_pago = form.cleaned_data['metodo_pago']
        
        venta = procesar_venta(
            self = self,
            tipo_venta = tipo_venta,
            metodo_pago = metodo_pago,
            usuario = self.request.user,
        )
        
        if venta: 
            return HttpResponseRedirect(reverse('ventas_app:venta_voucher_pdf', kwargs={'pk': venta.pk }))
            
        else:
            return HttpResponseRedirect(reverse('ventas_app:agregar_carrito'))

        #return HttpResponseRedirect(reverse('ventas_app:agregar_carrito'))


#
class ProcesoVenta(LoginRequiredMixin, generic.FormView):
    form_class = VentaVoucherForm
    success_url = '.'
    
    def form_valid(self, form):
        tipo_venta = form.cleaned_data['tipo_venta']
        metodo_pago = form.cleaned_data['metodo_pago']
        
        venta = procesar_venta(
            self = self,
            tipo_venta = tipo_venta,
            metodo_pago = metodo_pago,
            usuario = self.request.user,
        )
        
        return HttpResponseRedirect(reverse('ventas_app:agregar_carrito'))
        


#
class VentaVoucherPdf(LoginRequiredMixin, SuccessMessageMixin, generic.View):
    
    def get(self, request, *args, **kwargs):
        venta = Venta.objects.get(id=self.kwargs['pk'])
        data = {
            'venta': venta,
            'detalle_productos': VentaDetalle.objects.filter(venta__id=self.kwargs['pk'])
        }
        pdf = render_to_pdf('ventas/voucher.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

       

#
class UltimasVentas(LoginRequiredMixin, generic.ListView):
    template_name = 'ventas/ultimas_ventas.html'
    context_object_name = 'ultimas_ventas'

    def get_queryset(self):
        return Venta.objects.ultimas_ventas()

    
    


#
@login_required(login_url='beses:login')
@permission_required('ventas.change_venta', login_url='bases:login')
def venta_anular(request, pk):
    if request.method == 'POST':
        venta = Venta.objects.filter(id=pk).first()
        venta.venta_anulada = True
        venta.save()

        VentaDetalle.objects.restablecer_stok_num_ventas(pk)

        return HttpResponse('OK')
    



#
class VentasDetalle(LoginRequiredMixin, SuccessMessageMixin, generic.DetailView):
    model = VentaDetalle
    permission_required = "ventas.view_venta"
    template_name = 'ventas/ventas_detalle.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)

        context['venta'] = Venta.objects.get(id=self.kwargs['pk'])
        context["detalle_venta"] = VentaDetalle.objects.filter(venta__id=self.kwargs['pk'])

        return context


#
# class SaleDeleteView(LoginRequiredMixin, generic.DeleteView):
#     template_name = "venta/delete.html"
#     model = Sale
#     success_url = reverse_lazy('venta_app:venta-index')

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.anulate = True
#         self.object.save()
#         # actualizmos sl stok y ventas
#         SaleDetail.objects.restablecer_stok_num_ventas(self.object.id)
#         success_url = self.get_success_url()

#         return HttpResponseRedirect(success_url)