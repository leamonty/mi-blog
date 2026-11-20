
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'fecha_creacion',
        'fecha_actualizacion',
    )

    search_fields = ('titulo', 'contenido')
    ordering = ('-fecha_creacion',)
