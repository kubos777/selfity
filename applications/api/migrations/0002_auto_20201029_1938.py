# Generated by Django 3.0.5 on 2020-10-29 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Formato 10 dígitos máximo', regex='^(\\d{10})$')]),
        ),
    ]
