from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    archivo_imagen = models.CharField(max_length=100)

class Interaccion(models.Model):
    # tuve que poner "nose" porque no dejaba poner "usuario", "usuario_base", "user"
    nose = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='nose_interaccion')
    # seguido: si gabo sigue a marcos --> nose: gabo, seguido: marcos
    seguido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguido_interaccion')

class Actividad_Reciente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_contenido = models.IntegerField()
    tipo_actividad = models.CharField(max_length=50)
    hora_fecha = models.DateTimeField()

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    link_referencia = models.CharField(max_length=100)
    biografia = models.CharField(max_length=10000)
    archivo_imagen = models.CharField(max_length=100)

class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    link_referencia = models.CharField(max_length=100)
    archivo_imagen = models.CharField(max_length=100)

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class Review(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=10000)
    puntaje = models.IntegerField()

class Lista(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    archivo_imagen = models.CharField(max_length=100)

class Albums_x_Lista(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class Artistas_Favoritos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

class Albums_Favorits(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)