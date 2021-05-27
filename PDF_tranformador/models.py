from PDF_Reader.settings import BASE_DIR
from django.core.files.storage import default_storage
from django.db import models

# Create your models here.

class Archivo(models.Model):
    # Atributos en la tabla

    archivo = models.FileField(
        blank=False,
        null=False
    )