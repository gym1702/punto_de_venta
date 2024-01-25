from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'telefono', 'tipo', 'cod_registro', 'num_registro',)
    list_filter = ['tipo', 'is_staff', 'is_active',]
    search_fields = ['full_name', 'email', 'telefono',]
    list_per_page = 10


admin.site.register(User, UserAdmin)