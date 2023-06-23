from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigo=models.CharField(primary_key=True, max_length=8, verbose_name="Codigo")
    marca= models.CharField(max_length=50, verbose_name="Marca")
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.codigo