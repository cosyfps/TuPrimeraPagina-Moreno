from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    TemplateView,
)

from .forms import * 
from .models import *

# Create your views here.

## * Main page
class index(LoginRequiredMixin, View): # * Arreglado el problema de iniciar a 'administracion/' sin logearse 
    def get(self, request):
        template = 'core/index.html'
        
        return render(request, template)    

# class error404(TemplateView):
#     template_name = 'core/error404.html'


## * Create Models (form)
class ClienteFormCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/clientes_form.html'
    success_url = 'list'


class DoctorFormCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctores_form.html'
    success_url = 'list'


class MascotaFromCreateView(LoginRequiredMixin, CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'core/mascotas_form.html'
    success_url = 'list'

class ConsultaFromCreateView(LoginRequiredMixin, CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'core/consultas_form.html'
    success_url = 'list'

## Read Models (list)
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'core/clientes_list.html'


class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'core/doctores_list.html'


class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'core/mascotas_list.html'


class ConsultaListView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'core/consultas_list.html'


## * Update Models (Update)
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/clientes_form.html'
    success_url = 'list'


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctores_form.html'
    success_url = 'list'  


class MascotaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'core/mascotas_form.html'
    success_url = 'list'


class ConsultaUpdateView(LoginRequiredMixin, UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'core/consultas_form.html'
    success_url = 'list'


## * Delete Models (Delete)
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'core/clientes_delete.html'
    success_url = 'list'


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'core/doctores_delete.html'
    success_url = 'list'


class MascotaDeleteView(LoginRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'core/mascotas_delete.html'
    success_url = 'list'


class ConsultaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = 'core/consultas_delete.html'
    success_url = 'list'

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form":form})

# ---------------------------------------------------------------------

# ! Configuracion Email

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def visitas(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        
        default_message = f"Correo: {email}\n\n{message}"
        
        send_mail(
            name, 
            default_message,  
            email, 
            ['kelvin.morenog28@gmail.com'],
            fail_silently=False
        )

    return render(request, "core/visitas.html")


