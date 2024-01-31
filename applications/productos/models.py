from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from applications.proveedores.models import Proveedor
from applications.categorias.models import Categoria
from applications.marcas.models import Marca

from .managers import ProductoManager



#
class Producto(models.Model):

    unidad = (
        ('pza', 'pza'),
        ('kg', 'kg'),
        ('l', 'l'),
    )

    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=7, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=7, decimal_places=2)
    no_ventas = models.PositiveIntegerField(blank=True, null=True, default=0)
    imagenes = models.ImageField(upload_to='fotos/productos', blank=True, null=True)
    stock = models.IntegerField()
    unidad = models.CharField(max_length=50, choices=unidad, default='pza')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    descuento = models.FloatField("Porcentaje de descuento", default= 0.0)
    fecha_inicio_descuento = models.DateField("Fecha de inicio de descuento", null=True, blank=True)
    fecha_fin_descuento = models.DateField("Fecha de fin de descuento", null=True, blank=True)

    objects = ProductoManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre



#
# class Descuento(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     descuento = models.FloatField("Porcentaje")
#     fecha_inicio = models.DateField()
#     fecha_fin = models.DateField()

#     def __str__(self):
#         return str(self.producto.nombre) + ' - ' + str(self.descuento)

#     class Meta:
#         verbose_name_plural = 'Descuentos'




#GUARDA UNA IMAGEN POR DEFAUL SI NO TIENE UNA ASIGNADA AL CREAR EL REGISTRO
@receiver(post_save, sender=Producto)
def save_image(sender, instance, created, **kwargs):
    # Verifica si se ha creado un nuevo registro y si tiene una imagen
    if created and not instance.imagenes:
        # Guarda la imagen en el registro
        instance.imagenes = 'logos/logo1.jpg'
        instance.save()

