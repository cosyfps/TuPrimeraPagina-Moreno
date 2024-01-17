from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.TipoCliente)
admin.site.register(models.Cliente)
admin.site.register(models.EspecialidadDoctor)
admin.site.register(models.Doctor)
admin.site.register(models.Mascota)
admin.site.register(models.Consulta)
