from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("registro/", views.registro_usuario, name="registro"),                                            #Pagina de resgistro de usuarios
   path("categorias/", views.categorias_subastas, name="categorias"),                           #Pagina de que muestra las categorias
   #path("categorias/<str:nombre>", views.articulos_categoria),                                           #Subpagina de articulos          
   path("productos/", views.articulos_categoria, name="articulos"),
   path("ofertar/", views.ofertar, name="ofertar"),


   #login de usuario
   path('login/', auth_views.LoginView.as_view(
      template_name = "./subastas_app/login.html"),
      name= 'login'),
   path('logout/', auth_views.LogoutView.as_view(
      next_page ="/"),
      name = 'logout')
]