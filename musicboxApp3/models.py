from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    archivo_imagen = models.CharField(max_length=100)

class Album(models.Model):
    artista = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    link_referencia = models.CharField(max_length=100)
    archivo_imagen = models.CharField(max_length=100)

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class Lista(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    archivo_imagen = models.CharField(max_length=100)

class Albums_x_Lista(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)