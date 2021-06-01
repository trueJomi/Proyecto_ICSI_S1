##  File Forms

# Django

from django import forms
from django.forms import fields
from PDF_tranformador.models import Archivo

class fileForm(forms.ModelForm):
    # file Model form
    class Meta:
        model= Archivo
        fields = (
            'archivo',
        )