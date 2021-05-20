from django.db import models


# Create your models here.

class Transaccion(models.Model):
    numero_cuenta = models.IntegerField(unique=True)
    numero_comprobante = models.CharField(max_length=20)
    tipo_comprobante = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=1000, blank=True, null=True)
    debito = models.DecimalField(max_digits=10, decimal_places=2)
    credito = models.DecimalField(max_digits=10, decimal_places=2)

