
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publicacion',
            new_name='Post',
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='posts/'
            ),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='posts',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RemoveField(
            model_name='post',
            name='publicada',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fecha_creacion']},
        ),
    ]
