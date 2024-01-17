from django.db import models

# Create your models here.
class TipoCliente(models.Model):
    tipoCliente = models.CharField(max_length=100, null=False, blank=False, default="")

    def __str__(self):
        return f"{self.tipoCliente}"

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=100, null=False, blank=False)
    apellidoCliente = models.CharField(max_length=100, null=False, blank=False)
    emailCliente = models.EmailField(max_length=100, null=True, blank=True)
    tipoCliente = models.ForeignKey(TipoCliente, null=True, blank=True, on_delete = models.CASCADE)
    direccionCliente = models.CharField(max_length=100, null=True, blank=True)
    edadCliente = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombreCliente}"
    
    class Model:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

class EspecialidadDoctor(models.Model):
    especialidadDoctor = models.CharField(max_length=100, null=False, blank=False, default="")

    def __str__(self):
        return f"{self.especialidadDoctor}"

class Doctor(models.Model):
    nombreDoctor = models.CharField(max_length=100, null=False, blank=False)
    apellidoDoctor = models.CharField(max_length=100, null=False, blank=False)
    emailDoctor = models.EmailField(max_length=100, null=True, blank=True)
    especialidadDoctor = models.ForeignKey(EspecialidadDoctor, null=True, blank=True, on_delete = models.CASCADE)
    direccionDoctor = models.CharField(max_length=100, null=True, blank=True)
    edadDoctor = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombreDoctor}, {self.especialidadDoctor}"
    
    class Model:
        verbose_name = "doctor"
        verbose_name_plural = "doctores"

class Mascota(models.Model):
    nombreMascota = models.CharField(max_length=100, null=False, blank=False)
    razaMascota = models.CharField(max_length=100, null=False, blank=False)
    descripcionMascota = models.CharField(max_length=100, null=True, blank=True)
    fechanacimientoMascota = models.DateField(null=False, blank=False)
    nombreDueno = models.ForeignKey(Cliente, null=True, blank=True, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.nombreMascota}, {self.razaMascota}"
    
    class Model:
        verbose_name = "mascota"
        verbose_name_plural = "mascotas"

class Consulta(models.Model):
    nombreConsulta = models.CharField(max_length=100, null=False, blank=False)
    descipcionConsulta = models.CharField(max_length=100, null=False, blank=False)
    fechaConsulta = models.DateField(null=False, blank=False)
    doctorConsulta = models.ForeignKey(Doctor, null=True, blank=True, on_delete = models.CASCADE)
    duenoConsulta = models.ForeignKey(Cliente, null=True, blank=True, on_delete = models.CASCADE)
    mascotaConsulta = models.ForeignKey(Mascota, null=True, blank=True, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.nombreConsulta}, {self.fechaConsulta}, {self.doctorConsulta}, {self.mascotaConsulta}"
    
    class Model:
        verbose_name = "consulta"
        verbose_name_plural = "consultas"
