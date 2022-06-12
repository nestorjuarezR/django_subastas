from django.shortcuts import render
from .models import Categorias
                             
# Create your views here.

'''Funcion que muestra el index'''
def index(request):
    '''Pagina Index'''
    return render(request, "./subastas_app/index.html")

'''Funcion que muestra la pagina de registro'''
def registro_usuario(request):

    return render(request, "./subastas_app/registro.html",)

'''Funcion que muestra la pagina con las categorias'''
def categorias_subastas(request):
    categorias_all = Categorias.objects.all()   #Consulta y selecciona todas las categorias registras
    return render(request, "./subastas_app/categorias.html",
    {
        "categorias": categorias_all
    })