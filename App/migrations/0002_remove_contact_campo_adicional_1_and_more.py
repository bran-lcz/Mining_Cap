# Generated by Django 4.2.6 on 2023-12-18 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='campo_adicional_1',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='campo_adicional_2',
        ),
    ]
