from django.contrib import admin

from .models import Marca


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_per_page = 10


admin.site.register(Marca, MarcaAdmin)

