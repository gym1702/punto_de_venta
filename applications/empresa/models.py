from django.db import models


#
class Empresa(models.Model):
    nombre = models.CharField('Nombre', max_length=200, null=True, blank=True)
    nombre_corto = models.CharField('Nombre', max_length=50, null=True, blank=True)
    eslogan = models.CharField('Eslogan', max_length=200, null=True, blank=True)
    calle = models.CharField('Calle', max_length=200)
    numero = models.CharField('Numero', max_length=10)
    colonia = models.CharField('Colonia', max_length=100)
    referencia = models.CharField('Referencia', max_length=100, null=True, blank=True)
    ciudad = models.CharField('Ciudad', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    pais = models.CharField('Pais', max_length=50, null=True, blank=True)
    cp = models.CharField('Codigo Postal', max_length=5, null=True, blank=True)
    telefono = models.CharField('telefono', max_length=10)
    web = models.CharField('Pagina web', max_length=200, null=True, blank=True)
    email = models.CharField('Email', max_length=200, null=True, blank=True)
    logo_principal = models.ImageField(upload_to='logos/', null=True, blank=True)
    logo_secundario = models.ImageField(upload_to='logos/', null=True, blank=True)
    #favicon = models.ImageField(upload_to='logos/', default='./media/logo.png', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Empresa"