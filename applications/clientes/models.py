from django.db import models

#from applications.users.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver


#
class Cliente(models.Model):
    credito = (
        ('Si', 'Si'),
        ('No', 'No'),
    )

    razon_social =  models.CharField('Razon social', max_length=100)
    rfc = models.CharField('RFC', max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=10) 
    email = models.EmailField(max_length=100)
    calle_no = models.CharField(max_length=200) 
    colonia = models.CharField(max_length=200) 
    ciudad = models.CharField(max_length=200) 
    estado = models.CharField(max_length=200) 
    cp = models.CharField(max_length=10) 
    cod_registro = models.CharField(max_length=20, null=True, blank=True)
    activo = models.BooleanField(default=True)
    credito = models.CharField(max_length=2, choices=credito, default='No')

    def __str__(self):
        return self.razon_social
    
    def direccion(self):
        return self.calle_no + ', ' + self.colonia + ', ' + self.ciudad + ', ' + self.estado
    
    # def save(self, *args, **kwargs):
    #     self.razon_social = (self.razon_social).upper()
    #     self.rfc = (self.rfc).upper()   
    #     self.email = (self.email).lower()
    #     return super(Cliente, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Clientes"



# #
# @receiver(post_save, sender=Cliente)
# def actualiza_usuario(sender, instance, **kwargs):
#     num_reg = instance.num_registro
            
#     user = User.object.filter(num_registro = num_reg).first()

#     if user:
#         user.email = instance.email
#         user.telefono = instance.telefono
#         user.razon_social = instance.razon_social
#         user.tipo = 'Cliente'
    
#         user.save()
  

