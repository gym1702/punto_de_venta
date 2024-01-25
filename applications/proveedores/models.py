from django.db import models



class Proveedor(models.Model):
    credito = (
        ('Si', 'Si'),
        ('No', 'No'),
    )

    razon_social =  models.CharField('Razon social', max_length=100)
    rfc = models.CharField('RFC', max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=10) 
    email = models.EmailField(max_length=100)
    web = models.CharField(max_length=100, blank=True, null=True)
    calle_no = models.CharField(max_length=200, blank=True, null=True) 
    colonia = models.CharField(max_length=200, blank=True, null=True) 
    ciudad = models.CharField(max_length=200, blank=True, null=True) 
    estado = models.CharField(max_length=200, blank=True, null=True) 
    cp = models.CharField(max_length=10, blank=True, null=True) 
    activo = models.BooleanField(default=True)
    credito = models.CharField(max_length=2, choices=credito, default='No')
    que_vende = models.CharField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.razon_social
    
    def direccion(self):
        return self.calle_no + ', ' + self.colonia + ', ' + self.ciudad + ', ' + self.estado

    
    class Meta:
        verbose_name_plural = "Proveedores"
