from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Tienda)
admin.site.register(models.Producto)
admin.site.register(models.Cliente)
admin.site.register(models.Boleta)