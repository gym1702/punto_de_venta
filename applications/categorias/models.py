from django.db import models



class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    descripcion = models.CharField('Descripcion', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Categorias'
