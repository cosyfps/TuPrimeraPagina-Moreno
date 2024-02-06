from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    # 
    path('clientes/list', views.ClienteListView.as_view(), name='clientes_list'),
    path('clientes/form', views.ClienteFormCreateView.as_view(), name='clientes_form'),
    path('clientes/update/<int:pk>', views.ClienteUpdateView.as_view(), name='clientes_update'),
    path('clientes/delete/<int:pk>', views.ClienteDeleteView.as_view(), name='clientes_delete'),
    # 
    path('doctores/list', views.DoctorListView.as_view(), name='doctores_list'),
    path('doctores/form', views.DoctorFormCreateView.as_view(), name='doctores_form'),
    path('doctores/update/<int:pk>', views.DoctorUpdateView.as_view(), name='doctores_update'),
    path('doctores/delete/<int:pk>', views.DoctorDeleteView.as_view(), name='doctores_delete'),
    # 
    path('mascotas/list', views.MascotaListView.as_view(), name='mascotas_list'),
    path('mascotas/form', views.MascotaFromCreateView.as_view(), name='mascotas_form'),
    path('mascotas/update/<int:pk>', views.MascotaUpdateView.as_view(), name='masscotas_update'),
    path('mascotas/delete/<int:pk>', views.MascotaDeleteView.as_view(), name='mascotas_delete'),
    # 
    path('consultas/list', views.ConsultaListView.as_view(), name='consultas_list'),
    path('consultas/form', views.ConsultaFromCreateView.as_view(), name='consultas_form'),
    path('consultas/update/<int:pk>', views.ConsultaUpdateView.as_view(), name='consultas_update'),
    path('consultas/delete/<int:pk>', views.ConsultaDeleteView.as_view(), name='consultas_delete'),
]
