# Generated by Django 3.0.5 on 2020-10-30 16:28

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201029_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('MIMEType', models.CharField(max_length=20, null=True, verbose_name='Tipo de imagen')),
                ('hashtag', models.CharField(max_length=20, unique=True, verbose_name='Nombre')),
                ('coords', models.CharField(max_length=500, verbose_name='Coordenadas')),
                ('file', models.ImageField(upload_to='images')),
                ('thumbnail', models.ImageField(null=True, upload_to='thumbnails')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
