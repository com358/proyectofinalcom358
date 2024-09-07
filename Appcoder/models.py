from django.db import models

class Visitantes(models.Model):
    nombre = models.CharField(max_length=15)
    color_favorito = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre}, {self.color_favorito}"

class Usuarios(models.Model):
    nombre = models.CharField(max_length=15)
    mail = models.EmailField(max_length=35)
    color_favorito = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre},{self.mail}, {self.color_favorito}"

class Moderadores(models.Model):
    nombre = models.CharField(max_length=15)
    mail = models.EmailField(max_length=35)
    password = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.nombre}, {self.mail}, {self.password}"