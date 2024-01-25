from django.contrib import admin

from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion',)
    search_fields = ('nombre',)
    list_per_page = 10



admin.site.register(Categoria, CategoriaAdmin)

