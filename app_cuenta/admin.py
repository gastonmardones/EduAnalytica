from django.contrib import admin
from .models import Transaccion

# Register your models here.


class Transaccion_Admin(admin.ModelAdmin):
    list_display = ('numero_cuenta', 'numero_comprobante', 'tipo_comprobante')


admin.site.register(Transaccion, Transaccion_Admin)