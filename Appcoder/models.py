from django.db import models

# Create your models here.

class Visitantes(models.Model):
    nombre = models.CharField(max_length=15)
    color_favorito = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre = models.CharField(max_length=15)
    edad = models.IntegerField
    mail = models.EmailField(max_length=35)
    color_favorito = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Moderadores(models.Model):
    nombre = models.CharField(max_length=15)
    mail = models.EmailField(max_length=35)
    password = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre

