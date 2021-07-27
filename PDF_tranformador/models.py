from django.db import models

# Create your models here.

class Archivo(models.Model):
    # Atributos en la tabla

    archivo = models.FileField(
        blank=False,
        null=False
    )
class Datos(models.Model):
    tipo_dato = models.CharField(max_length=1)
    voz = models.CharField(max_length=1)
    velocidad= models.DecimalField(max_digits=3, decimal_places=0)