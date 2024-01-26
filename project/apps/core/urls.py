from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="visitas"),
    # 
    path('cliente/list', views.clientes_list, name='clientes_list'),
    path('clientes/form', views.clientes_form, name='clientes_form'),
    # 
    path('doctores/list', views.doctores_list, name='doctores_list'),
    path('doctores/form', views.doctores_form, name='doctores_form'),
    # 
    path('mascotas/list', views.mascotas_list, name='mascotas_list'),
    path('mascotas/form', views.moscotas_form, name='mascotas_form'),
    # 
    path('consultas/list', views.consultas_list, name='consultas_list'),
    path('consultas/form', views.consultas_form, name='consultas_form'),
]
