from django.shortcuts import render, redirect
from app_cuenta.forms import Form
from app_cuenta.models import Transaccion

# Create your views here.

def transaccion_new(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/accounts/')
    else:
        form = Form()

    return render(request, 'forms/forms.html', {'form': form})


def accounts(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'app_cuenta/index.html', {'transacciones': transacciones})


def blank(request):
    return render(request, 'blank/blank.html')
