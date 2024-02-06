from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import * 
from .models import *

# Create your views here.

## * Main page
def index(request):
    return render(request, "core/index.html")


## * Create Models (form)
class ClienteFormCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/clientes_form.html'
    success_url = 'list'


class DoctorFormCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctores_form.html'
    success_url = 'list'


class MascotaFromCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'core/mascotas_form.html'
    success_url = 'list'

class ConsultaFromCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'core/consultas_form.html'
    success_url = 'list'

## Read Models (list)
class ClienteListView(ListView):
    model = Cliente
    template_name = 'core/clientes_list.html'


class DoctorListView(ListView):
    model = Doctor
    template_name = 'core/doctores_list.html'


class MascotaListView(ListView):
    model = Mascota
    template_name = 'core/mascotas_list.html'


class ConsultaListView(ListView):
    model = Consulta
    template_name = 'core/consultas_list.html'


## * Update Models (Update)
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = 'list'


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    success_url = 'list'  


class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    success_url = 'list'


class ConsultaUpdateView(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    success_url = 'list'


## * Delete Models (Delete)
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = 'list'


class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = 'list'


class MascotaDeleteView(DeleteView):
    model = Mascota
    success_url = 'list'


class ConsultaDeleteView(DeleteView):
    model = Consulta
    success_url = 'list'