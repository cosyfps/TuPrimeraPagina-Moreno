from django.shortcuts import redirect, render

from . import models 
from . import forms

# Create your views here.

## * Main page
def index(request):
    return render(request, "core/visitas.html") # TODO: core/visitas.html


## * Create Models (form)
def clientes_form(request):
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes_list")
    else:
        form = forms.ClienteForm()
    return render(request, "core/clientes_form.html", {"form" : form})

def doctores_form(request):
    if request.method == 'POST':
        form = forms.DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctores_list")
    else:
        form = forms.DoctorForm()
    return render(request, "core/doctores_form.html", {"form" : form})

def moscotas_form(request):
    if request.method == 'POST':
        form = forms.MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mascotas_list")
    else:
        form = forms.MascotaForm()
    return render(request, "core/mascotas_form.html", {"form" : form})

def consultas_form(request):
    if request.method == 'POST':
        form = forms.ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consultas_list")
    else:
        form = forms.ConsultaForm()
    return render(request, "core/consultas_form.html", {"form" : form})


## * Read Models (list)
def clientes_list(request):
    consulta = models.Cliente.objects.all()
    context = {"Cliente" : consulta}
    return render(request, "core/clientes_list.html", context)

def doctores_list(request):
    consulta = models.Doctor.objects.all()
    context = {"Doctor" : consulta}
    return render(request, "core/doctores_list.html", context)

def mascotas_list(request):
    consulta = models.Mascota.objects.all()
    context = {"Mascota":consulta}
    return render(request, "core/mascotas_list.html", context)

def consultas_list(request):
    consulta = models.Consulta.objects.all()
    context = {"Consulta":consulta}
    return render(request, "core/consultas_list.html", context)


## TODO: Update Models (Update)
## TODO: Delete Models (Delete)

