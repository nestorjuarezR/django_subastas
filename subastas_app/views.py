from django.shortcuts import render

# Create your views here.


def index(reques):
    '''Pagina Index'''
    return render(reques, "./subastas_app/index.html")