from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import VentaManager, VentaDetalleManager, CarritoManager

from applications.productos.models import Producto



class Venta(models.Model):
    tipo = (
        ('Nota', 'Nota'),
        ('Factura', 'Factura'),
        ('Sin comprobante', 'Sin comprobante'),
    )

    metodo = (
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
        ('Deposito', 'Deposito'),
        ('Otro', 'Otro'),
    )

    fecha = models.DateTimeField()
    #cantidad = models.PositiveIntegerField()
    cantidad = models.FloatField()
    iva = models.FloatField()
    subtotal = models.FloatField()
    descuento = models.FloatField()
    monto = models.FloatField() # almacena monto antes de iva
    monto_iva = models.FloatField() # almacena monto iva incluido
    tipo_venta = models.CharField(max_length=50, choices=tipo, default='Nota')
    metodo_pago = models.CharField(max_length=50, choices=metodo, default='Nota')
    venta_cerrada = models.BooleanField(default=False)
    venta_anulada = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    objects = VentaManager()

    class Meta:
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return 'No. [' + str(self.id) + '] - ' + str(self.fecha)
    

#
class VentaDetalle(models.Model):

    ## MOTA: El related_name se utiliza para hacer la conexion entra venta y detale venta
    ## ver functions.py de caja para ver su uso
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    #cantidad = models.PositiveIntegerField()
    cantidad = models.FloatField()
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    iva = models.FloatField()
    anulada = models.BooleanField(default=False)
    subtotal = models.FloatField(null=True, blank=True)
    descuento =  models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    fecha = models.DateTimeField()
    
    objects = VentaDetalleManager()

    def __str__(self):
        return  str(self.venta.id) + ' - ' + str(self.producto.nombre)
    
   
    
    class Meta:
        verbose_name_plural = 'Detalles'


#
class Carrito(models.Model):
    codigo = models.CharField(max_length=50)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE )
    #cantidad = models.PositiveIntegerField()
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    objects = CarritoManager()

    class Meta:
        verbose_name_plural = 'Carritos de compras'

    def __str__(self):
        return  str(self.producto.nombre)
    

