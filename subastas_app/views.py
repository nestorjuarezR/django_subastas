from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria, User
                             
# Create your views here.

'''Funcion que muestra el index'''
def index(request):
    '''Pagina Index'''
    return render(request, "./subastas_app/index.html")

'''Funcion que muestra la pagina de registro'''
def registro_usuario(request):

    if request.method == "POST":
        nuevo_usuario = User()
        nuevo_usuario.first_name = request.POST['first_name']
        nuevo_usuario.last_name = request.POST['last_name']
        nuevo_usuario.genere = request.POST['genere']
        nuevo_usuario.date_birth = request.POST['date_birth']
        nuevo_usuario.username = request.POST['username']
        nuevo_usuario.email = request.POST['email']
        next = request.GET.get("next", "/")
        nuevo_usuario.save()
      
        return redirect(next)


    return render(request, "./subastas_app/registro.html")


'''Funcion para la pagina ofertar (Obligatorio el login)'''
@login_required(login_url='/login/')
def ofertar(request):
    return render(request,"./subastas_app/ofertar.html")


'''Funcion que muestra la pagina con las categorias'''
def categorias_subastas(request):
    categorias_all = Categoria.objects.all()   #Consulta y selecciona todas las categorias registras
    return render(request, "./subastas_app/categorias.html",
    {
        "categorias": categorias_all
    })