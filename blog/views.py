
from django.shortcuts import render
from .models import Post


def inicio(request):
    publicaciones = Post.objects.all()

    contexto = {
        'publicaciones': publicaciones
    }

    return render(request, 'blog/inicio.html', contexto)
