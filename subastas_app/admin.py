from django.contrib import admin
from .models import Categoria, User

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_categorias = ("nombre", "descripcion")

class UsuarioAdmin(admin.ModelAdmin):
    list = ("username", "email")



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(User,UsuarioAdmin)
