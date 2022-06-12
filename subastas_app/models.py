from django.db import models

# Create your models here.



#Modelo de categorias
class Categorias(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    descripcion = models.CharField(max_length=250, null=False, blank=False)
    category_image = models.ImageField(upload_to='media/' ,max_length=100, null=True)

    def __str__(self):
        return self.nombre