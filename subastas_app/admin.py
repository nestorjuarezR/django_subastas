from django.contrib import admin
from .models import Categoria, User, Articulo, Subasta

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_categorias = ("nombre", "descripcion")

class UsuarioAdmin(admin.ModelAdmin):
    list = ("username", "email")

class ArticuloAdmin(admin.ModelAdmin):
    lista = ("nombre", "categoria", )

class SubastaAdmin(admin.ModelAdmin):
    lista = ("articulo", "user_ganador")



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(User,UsuarioAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Subasta,SubastaAdmin)