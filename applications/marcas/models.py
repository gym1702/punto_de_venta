from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre
