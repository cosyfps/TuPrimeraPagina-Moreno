from django.shortcuts import redirect, render

from . import models 
from . import forms

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def tienda_list(request):
    consulta = models.Tienda.objects.all()
    context = {"Tienda" : consulta}
    return render(request, "core/tienda_list.html", context)

def tienda_form(request):
    if request.method == 'POST':
        form = forms.TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda_list")
    else:
        form = forms.TiendaForm()
    return render(request, "core/tienda_form.html", {"form" : form})