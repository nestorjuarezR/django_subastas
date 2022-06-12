from django.contrib import admin
from .models import Categorias

# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    list_categorias = ("nombre", "descripcion")


admin.site.register(Categorias, CategoriasAdmin)
