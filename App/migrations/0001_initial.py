# Generated by Django 4.2.6 on 2023-12-17 23:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=120)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('apellidos', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('metodos_contacto', models.CharField(blank=True, max_length=255, null=True)),
                ('servicio_preferido', models.CharField(blank=True, max_length=255, null=True)),
                ('campo_adicional_1', models.CharField(blank=True, max_length=50, null=True)),
                ('campo_adicional_2', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
