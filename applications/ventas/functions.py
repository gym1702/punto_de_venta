#
from django.utils import timezone
from django.db.models import Prefetch
#
from applications.productos.models import Producto
#
from .models import Venta, VentaDetalle, Carrito


def procesar_venta(self, **params_venta):
    # recupera la lista de productos en carrtio
    productos_en_car = Carrito.objects.all()
    
    if productos_en_car.count() > 0:
        
        # crea el objeto venta
        venta = Venta.objects.create(
            fecha = timezone.now(),
            cantidad = 0.0,
            monto = 0.0,
            tipo_venta = params_venta['tipo_venta'],
            metodo_pago = params_venta['metodo_pago'],
            usuario = params_venta['usuario'],
            iva = 0.0,
            subtotal = 0.0,
            descuento = 0.0,
            monto_iva = 0.0,
        )
        
        ventas_detalle = []
        productos_en_venta = []

        for producto_car in productos_en_car:

            #VErifica si oferta esta vigente en base a fechas 
            vigente = False
            descuento = 0

            if producto_car.producto.fecha_inicio_descuento and producto_car.producto.fecha_fin_descuento:
                fecha_actual = timezone.now().date()

                if producto_car.producto.fecha_inicio_descuento <= fecha_actual <= producto_car.producto.fecha_fin_descuento:
                    vigente = True
                    #descuento = (float(producto_car.producto.precio_venta) / (1.16) * float(producto_car.producto.descuento) / float(100)) * float(producto_car.cantidad),


                    #llena carrito con productos
                    venta_detalle = VentaDetalle(
                        fecha = timezone.now(),
                        producto = producto_car.producto,
                        venta = venta,
                        cantidad = producto_car.cantidad,
                        precio_compra = producto_car.producto.precio_compra,
                        precio_venta = float(producto_car.producto.precio_venta) / (1.16),#(1.16) para quitar iva
                        iva = 0.16,
                        subtotal = float(producto_car.cantidad) * (float(producto_car.producto.precio_venta) / float(1.16)),
                        #descuento = descuento,
                        descuento = (float(producto_car.producto.precio_venta) / (1.16) * float(producto_car.producto.descuento) / float(100)) * float(producto_car.cantidad),
                        total = (float(producto_car.cantidad) * float(producto_car.producto.precio_venta) / (1.16)) - (float(producto_car.producto.precio_venta) / (1.16) * float(producto_car.producto.descuento) / float(100)) * float(producto_car.cantidad)
                        #total = (float(producto_car.cantidad) * float(producto_car.producto.precio_venta) / (1.16)) - float((float(producto_car.producto.precio_venta) / (1.16) * float(producto_car.producto.descuento) / float(100)) * float(producto_car.cantidad)) * float(producto_car.cantidad)
                    )
            

                    # actualizmos stok de producto en iteracion
                    producto = producto_car.producto
                    producto.stock = producto.stock - producto_car.cantidad
                    producto.no_ventas = producto.no_ventas + producto_car.cantidad
                    #Agrega productos a detalle de venta
                    ventas_detalle.append(venta_detalle)
                    productos_en_venta.append(producto)
                    #Calcula totales de venta
                    desc = ((float(venta_detalle.precio_venta) * float(producto_car.producto.descuento)) / float(100))
                    venta.cantidad = float(venta.cantidad) + float(producto_car.cantidad)
                    venta.subtotal = float(venta.monto) + float(producto_car.cantidad) * (float(producto_car.producto.precio_venta) / (1.16) - float(desc))
                    venta.monto = float(venta.monto) + float(producto_car.cantidad) * (float(producto_car.producto.precio_venta) / (1.16) - float(desc))
                    venta.iva = float(venta.monto) * float(venta_detalle.iva)
                    venta.monto_iva = venta.iva + venta.monto

                
                    venta.save()

                else:

                    #llena carrito con productos
                    venta_detalle = VentaDetalle(
                        fecha = timezone.now(),
                        producto = producto_car.producto,
                        venta = venta,
                        cantidad = producto_car.cantidad,
                        precio_compra = producto_car.producto.precio_compra,
                        precio_venta = float(producto_car.producto.precio_venta) / (1.16),#(1.16) para quitar iva
                        iva = 0.16,
                        subtotal = float(producto_car.cantidad) * (float(producto_car.producto.precio_venta) / float(1.16)),
                        descuento = 0.0,
                        #descuento = (float(producto_car.producto.precio_venta) / (1.16) * float(producto_car.producto.descuento) / float(100)) * float(producto_car.cantidad),
                        total = (float(producto_car.cantidad) * float(producto_car.producto.precio_venta) / (1.16))
                    )
            

                    # actualizmos stok de producto en iteracion
                    producto = producto_car.producto
                    producto.stock = producto.stock - producto_car.cantidad
                    producto.no_ventas = producto.no_ventas + producto_car.cantidad
                   
                    #Agrega productos a detalle de venta
                    ventas_detalle.append(venta_detalle)
                    productos_en_venta.append(producto)
                    
                    #Calcula totales de venta
                    #desc = ((float(venta_detalle.precio_venta) * float(producto_car.producto.descuento)) / float(100))
                    venta.cantidad = float(venta.cantidad) + float(producto_car.cantidad)
                    venta.subtotal = float(venta.monto) + float(producto_car.cantidad) * (float(producto_car.producto.precio_venta) / (1.16))
                    venta.monto = float(venta.monto) + float(producto_car.cantidad) * (float(producto_car.producto.precio_venta) / (1.16))
                    venta.iva = float(venta.monto) * float(venta_detalle.iva)
                    venta.monto_iva = venta.iva + venta.monto

                
                    venta.save()


        

        VentaDetalle.objects.bulk_create(ventas_detalle)
        # actualizamos el stok
        Producto.objects.bulk_update(productos_en_venta, ['stock', 'no_ventas'])
        # completada la venta, eliminamos productos del carrito
        productos_en_car.delete()
        return venta
    else:
        return None
    