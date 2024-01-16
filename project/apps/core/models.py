from django.db import models

# Create your models here.
class Tienda(models.Model):
    nombreTienda = models.CharField(max_length=100)
    ubicacionTienda = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombreTienda}"
    
    class Model:
        verbose_name = "tienda"
        verbose_name_plural = "tiendas"

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=100)
    valorProducto = models.IntegerField()
    fechaVencimiento = models.DateField(null=True, blank=True)
    tiendaCompra = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.nombreProducto}, {self.valorProducto}"
    
    class Model:
        verborse_name = "producto"
        verbose_name_plural = "productos"

class Cliente(models.Model):
    rutCliente = models.CharField(max_length=8)
    nombreCliente = models.CharField(max_length=100)
    apellidoCliente = models.CharField(null=True, blank=True, max_length=100)
    fechaNacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.rutCliente}, {self.nombreCliente}"

    class Model:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

class Boleta(models.Model):
    fechaEmision = models.DateField(null=False, blank=False)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.SET_NULL)
    tienda = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.fechaEmision}, {self.cliente}, {self.producto}, {self.tienda}"
