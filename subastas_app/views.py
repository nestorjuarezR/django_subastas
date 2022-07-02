from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Categoria, Subasta, User, Articulo
                             
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
        password = request.POST['password']
        nuevo_usuario.email = request.POST['email']
        nuevo_usuario.is_active = True
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()
        next = request.GET.get("next", "/login/")
        
      
        return redirect(next)


    return render(request, "./subastas_app/registro.html")


'''Funcion para la pagina ofertar (Obligatorio el login)'''
@login_required(login_url='/login/')
def ofertar(request):
    return render(request,"./subastas_app/ofertar.html")


'''Funcion que muestra la pagina con las categorias'''
def categorias_subastas(request):
    categorias_all = Categoria.objects.all()                                    #Consulta y selecciona todas las categorias registras
    return render(request, "./subastas_app/categorias.html",
    {
        "categorias": categorias_all
    })


'''Funcion que muestra la pagina de articulos de una categoria'''
def articulos_categoria(request, categoria_nombre):
    categoria = Categoria.objects.filter(nombre=categoria_nombre)
    articulos = Articulo.objects.all()
    #categorias = Categoria.objects.all()    
    print(articulos)
    return render(request, "./subastas_app/articulos.html",
    {
        'articulos': articulos,
        'categoria': categoria
    })


'''Funcion para mostrar la pagina de la subasta del articulo'''
def subasta_articulo(request,articulo_id):
    #Obtengo los objetos para el listado de informacion
    articulo_subasta = Subasta.objects.filter(articulo_id = articulo_id)
    articulo = Articulo.objects.filter(id=articulo_id)

    #Actualizacion del valor de ultima puja en html
    if request.method == "POST":
        ultima_puja = request.POST['precio_ganador']
        #usuario = request.user
        articulo_subasta.Precio_ganador = ultima_puja
        articulo_subasta.update(precio_ganador = ultima_puja)
        
        return redirect(request.META['HTTP_REFERER'])


    return render(request,"./subastas_app/subasta_articulo.html",
    {
        'articulo_subasta' : articulo_subasta,
        'articulo' : articulo,
    })


'''Funcion para que el usuario agrege articulos de una categoria'''
def agregar_articulo(request):
    #obtengo el nombre de las categorias
    categorias_all = Categoria.objects.all()     

    if request.method == "POST":
        nuevo_articulo = Articulo()
        user = request.user.id
        nombre = request.POST['nombre']
        categoria_id = request.POST['categoria_id']
        descripcion = request.POST['descripcion']
        precio_minimo = request.POST['precio_minimo']
        imagen = request.FILES['imagen']

        nuevo_articulo = Articulo(
            user_id = user,
            nombre = nombre,
            descripcion = descripcion,
            precio_minimo = precio_minimo,
            categoria_id = categoria_id,
            imagen = imagen
        )
        nuevo_articulo.save()
        return redirect("/categorias/")

    return render(request, "./subastas_app/agregar_articulo.html",{
        'categorias': categorias_all
    })


def perfil_usuario(request):
    info_user = User.objects.all()
    return render(request, "./subastas_app/user_profile.html",{
        'user_info': info_user
    })