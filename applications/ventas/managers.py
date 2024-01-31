# python
from datetime import timedelta
# django
from django.utils import timezone
from django.db import models
from django.db.models.functions import Cast
#
from applications.productos.models import Producto

from django.db.models import Q, Sum, F, FloatField, ExpressionWrapper, DateField


class VentaManager(models.Manager):
    """ procedimiento para modelo venta """
    
    #
    def ultimas_ventas(self):
        # creamos rango de fecha
        return self.filter(
            venta_cerrada=False,
            venta_anulada=False
        ).order_by('-id')

    
    #
    def total_ventas_dia(self):
        consulta = self.filter(
            venta_cerrada=False,
            venta_anulada=False
        ).aggregate(
            total=Sum('monto')
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0
        
      
    #
    def total_ventas_anuladas_dia(self):
        consulta = self.filter(
            venta_cerrada=False,
            venta_anulada=True
        ).aggregate(
            total=Sum('monto')
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0


    #
    def cerrar_ventas(self):
        consulta = self.filter(
            venta_cerrada=False,
        )
        # actualizmos a cerrado
        total = consulta.aggregate(
            total=Sum('monto')
        )['total']
        cerrados = consulta.update(venta_cerrada=True) # devuelve numero de actualizciones

        return cerrados, total
    

    #
    def total_ventas(self):
        return self.filter(
            venta_anulada=False,
        ).aggregate(
            total=Sum('monto')
        )['total']
    

    #
    def ventas_en_fechas(self, date_start, date_end):
        return self.filter(
            venta_anulada=False,
            fecha__range=(date_start, date_end),
        ).order_by('-fecha')



class VentaDetalleManager(models.Manager):
    """ procedimiento modelo product """
    
    #
    def detalle_por_venta(self, id_venta):
        return self.filter(
            venta__id=id_venta
        )


    #
    def ventas_mes_producto(self, id_prod):
        # creamos rango de fecha
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30)
        
        consulta = self.filter(
            venta__venta_anulada=False,
            fecha__range=(start_date, end_date),
            producto__pk=id_prod,
        ).values('venta__fecha', 'producto__nombre').annotate(
            cantidad_vendida=Sum('cantidad'),
        )
        return consulta
    
    
    #
    def restablecer_stok_num_ventas(self, id_venta):
        prods_en_anulados = []
        for venta_detail in self.filter(venta__id=id_venta):
            #actualizamos producto
            venta_detail.producto.stock = venta_detail.producto.stock + venta_detail.cantidad
            venta_detail.producto.no_ventas = venta_detail.producto.no_ventas - venta_detail.cantidad
            prods_en_anulados.append(venta_detail.producto)
        Producto.objects.bulk_update(prods_en_anulados, ['stock', 'no_ventas'])
        return True
    
    
    #
    def resumen_ventas(self):
        return self.filter(venta__venta_anulada=False, venta__venta_cerrada=True,
        ).values('venta__fecha__date').annotate(
            total_vendido=Sum(F('precio_venta')*F('cantidad'),output_field=FloatField()),
            total_ganancias=Sum(F('precio_venta')*F('cantidad') - F('precio_compra')*F('cantidad'),output_field=FloatField()),
            num_ventas=Sum('cantidad'),
        )
    

    def resumen_ventas_mes(self):
        #
        return self.filter(
            sale__anulate=False
        ).values('sale__date_sale__date__month', 'sale__date_sale__date__year').annotate(
            cantidad_ventas=Sum('count'),
            total_ventas=Sum(F('price_sale')*F('count'), output_field=FloatField()),
            ganancia_total=Sum(
                F('price_sale')*F('count') - F('price_purchase')*F('count'),
                output_field=FloatField()
            )
        ).order_by('-sale__date_sale__date__month')
    

    def resumen_ventas_proveedor(self, **filters):
        # recibe 3 parametros en un diccionario
        # devuelve lista de ventas en rango de fechas de un proveedor
        # y, devuelve el total de ventas en rango de fechas y de proveedor

        if filters['date_start'] and filters['date_end'] and filters['provider']:
            consulta = self.filter(
                anulate=False,
                sale__date_sale__range = (
                    filters['date_start'],
                    filters['date_end'],
                ),
                product__provider__pk=filters['provider'],
            )
            
            lista_ventas = consulta.annotate(
                sub_total=ExpressionWrapper(
                    F('price_purchase')*F('count'),
                    output_field=FloatField()
                )
            ).order_by('sale__date_sale')

            total_ventas = consulta.aggregate(
                total_venta=Sum(
                    F('price_purchase')*F('count'),
                    output_field=FloatField()
                )
            )['total_venta']

            return lista_ventas, total_ventas
        else:
            return [], 0
        



class CarritoManager(models.Manager):
    """ procedimiento modelo Carrito de compras """
    
    # def total_cobrar(self):
        
    #     descuento = (F('producto__precio_venta') * F('producto__descuento') /100) * F('cantidad')

    #     if descuento:

    #         consulta = self.aggregate(total=Sum(F('cantidad')*F(('producto__precio_venta')) - descuento, output_field=FloatField()),)
            
    #         if consulta['total']:
    #             return consulta['total']
    #         else:
    #             return 0 
             
    #     else:   
    #         consulta = self.aggregate(total=Sum(F('cantidad')*F(('producto__precio_venta')), output_field=FloatField()),)
            
    #         if consulta['total']:
    #             return consulta['total']
    #         else:
    #             return 0      



    def total_cobrar(self):

        fecha_actual = timezone.now().date()  

        consul = self.filter(producto__fecha_inicio_descuento__lte=fecha_actual, producto__fecha_fin_descuento__gte=fecha_actual)

            
        if consul.exists():

            descuento = (F('producto__precio_venta') * F('producto__descuento') /100) * F('cantidad')

            consulta = self.aggregate(total=Sum(F('cantidad')*F(('producto__precio_venta')) - descuento, output_field=FloatField()),)
            
            if consulta['total']:
                return consulta['total']
            else:
                return 0 
                    
        else:   

            consulta = self.aggregate(total=Sum(F('cantidad')*F(('producto__precio_venta')), output_field=FloatField()),)
            
            if consulta['total']:
                return consulta['total']
            else:
                return 0 
            


    #VERIFICA VIGENCIA DE DESCUENTO PARA USARSE EN TEMPLATE VENTAS
    # def vigencia(self):
                 
    #     fecha_actual = timezone.now().date()  

    #     consul = self.filter(producto__fecha_inicio_descuento__lte=fecha_actual, producto__fecha_fin_descuento__gte=fecha_actual)

    #     if consul.exists():
    #         return ['vigencia']
       