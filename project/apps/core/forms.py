from django import forms

from . import models


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = "__all__"

class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = "__all__"

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = models.Consulta
        fields = "__all__"