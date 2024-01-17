from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    # path('tienda/list', views.tienda_list, name="tienda_list"),    
]