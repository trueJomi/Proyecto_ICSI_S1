##  File Forms

# Django

from django import forms
from django.forms import fields
from PDF_tranformador.models import Archivo
from PDF_tranformador.models import Datos

class fileForm(forms.ModelForm):
    # file Model form
    class Meta:
        model= Archivo
        fields = (
            'archivo',
        )

class dataForm(forms.ModelForm):
    class Meta:
        model= Datos
        fields = (
            'tipo_dato','voz','velocidad',
        )
    