from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "password1": forms.PasswordInput(attrs={"class":"form-control"}),
            "password2": forms.PasswordInput(attrs={"class":"form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None