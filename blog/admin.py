from django.contrib import admin
from .models import Publicacion


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'autor',
        'fecha_creacion',
        'publicada'
    )

    list_filter = ('publicada', 'fecha_creacion')

    search_fields = ('titulo', 'contenido')

    ordering = ('-fecha_creacion',)