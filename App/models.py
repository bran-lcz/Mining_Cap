from django.db import models
from django.utils import timezone
from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    date = models.DateTimeField(default=timezone.now)

class Contact(models.Model):
    rut = models.CharField(max_length=15, null=False, unique=True)
    nombre = models.CharField(max_length=100, null=False, unique=True)
    apellidos = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    metodos_contacto = models.CharField(max_length=255, null=True, blank=True)
    servicio_preferido = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

    