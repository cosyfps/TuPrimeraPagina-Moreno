from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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

# -------------------------------------------------------
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields =["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }

