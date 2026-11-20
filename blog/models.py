
from django.db import models
from django.contrib.auth.models import User


class Publicacion(models.Model):

    titulo = models.CharField(max_length=200)

    contenido = models.TextField()

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='publicaciones'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
