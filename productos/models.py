from django.db import models

# Create your models here.

# Modelo para Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)

    def __str__(self):
        return self.nombre
