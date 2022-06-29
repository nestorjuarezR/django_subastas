from pyexpat import model
from django.db import models
from django.contrib.auth.models import  AbstractUser



# Create your models here.



#Modelo de categorias
class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False, blank=False)
    descripcion = models.CharField(max_length=250, null=False, blank=False)
    category_image = models.ImageField(upload_to='categorias' , null=True)
    url_name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.nombre}'

#Modificar-Extender el modelo Usur de Django

#Modelo Usuario
class User(AbstractUser):
    first_name = models.CharField(max_length=150, null=False, blank=False, unique=False)
    last_name = models.CharField(max_length=150, unique=False)
    GENERO = [
    ("H", "Hombre"),
    ("M", "Mujer"),
    ("O", "Otro"),
    ]
    genere = models.CharField(max_length=1, choices=GENERO)
    date_birth = models.DateField(null=True, blank=True)
    username = models.CharField(unique=True, max_length=20, null=False, blank=False)
    password = models.CharField(max_length=12, null=False, blank=False)
    email = models.EmailField(unique=True, null = False, blank=False)
    image = models.ImageField(upload_to='user_images', null=True, blank=True, default='./user_images/anonimo.svg')
    is_staff = models.BooleanField(default=False, blank=False, null=False)
    is_superuser = models.BooleanField(default=False, blank=False, null=False)
    is_active = models.BooleanField(default=True)


    def __sts__(self):
        return f'{self.username}, {self.email}'


#Modelo de Articulo

class Articulo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre =models.CharField( max_length=80, null=False, blank=False)
    descripcion = models.CharField(max_length=240, null=False, blank=False)
    precio_minimo = models.IntegerField(null=True, blank=True)
    imagen =  models.ImageField(upload_to='articulos_images', null=True)

    def __str__(self):
        return f'{self.nombre}, {self.descripcion}'

class Subasta(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE)
    user_ganador = models.OneToOneField(User, on_delete=models.CASCADE)
    precio_ganador = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Usuario ganador: {self.user_ganador}, Precio ganador: {self.precio_ganador}'