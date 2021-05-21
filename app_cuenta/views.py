from django.shortcuts import render
from app_cuenta.models import Transaccion

# Create your views here.

def accounts(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'app_cuenta/index.html', {'transacciones': transacciones})


