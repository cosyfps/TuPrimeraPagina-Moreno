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

# -------------------------------------------------------
        
class TuFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre Completo', required=True, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre...'}))
    email = forms.EmailField(label='Direccion de Email', required=True, max_length=30, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    contenido = forms.CharField(label='Mensaje', max_length=400, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje aquí...', 'style': 'height: 10rem; resize: none'}))

