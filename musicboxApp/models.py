from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50,null=False)
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



"""
DateField
DateTimeField
TimeField

toppings = models.ManyToManyField(Topping)
"""