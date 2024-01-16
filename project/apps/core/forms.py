from django import forms

from . import models 

class TiendaForm(forms.ModelForm):
    class Meta:
        model = models.Tienda
        fields = "__all__"