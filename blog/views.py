from django.shortcuts import render
from .models import Publicacion


def inicio(request):

    publicaciones = Publicacion.objects.filter(
        publicada=True
    ).order_by('-fecha_creacion')

    contexto = {
        'publicaciones': publicaciones
    }

    return render(request, 'blog/inicio.html', contexto)
