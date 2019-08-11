from django.db import models


class Actividad(models.Model):
    fecha_hora = models.DateTimeField()
    titulo = models.CharField(max_length=40)
