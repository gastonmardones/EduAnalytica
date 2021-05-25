from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from app_cuenta.forms import TransaccionForm
from app_cuenta.models import Transaccion
from django.views.generic import TemplateView, ListView, CreateView, UpdateView


# Create your views here.


class Blank(TemplateView):
    template_name = 'blank/blank.html'


class Accounts(ListView):
    template_name = 'app_cuenta/index.html'
    model = Transaccion
    # queryset = Transaccion.objects.all()      # Metodo predefinido dentro de ListView
    # context_object_name = 'transacciones'     # Sino usa como context: 'nombredelmodelo_list'


class TransaccionCreate(CreateView):
    model = Transaccion
    template_name = 'forms/forms.html'
    form_class = TransaccionForm
    success_url = reverse_lazy('accounts')


class TransaccionUpdate(UpdateView):
    model = Transaccion
    template_name = 'forms/forms.html'
    form_class = TransaccionForm
    success_url = reverse_lazy('accounts')


