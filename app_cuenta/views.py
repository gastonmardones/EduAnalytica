from django.shortcuts import render
from app_cuenta.forms import Form
from app_cuenta.models import Transaccion

# Create your views here.

def transaccion_new(request):
        form = Form(request.POST)
    return render(request, 'forms/forms.html', {'form': form})

def accounts(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'app_cuenta/index.html', {'transacciones': transacciones})


