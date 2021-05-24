from django.shortcuts import render, redirect
from app_cuenta.forms import Form
from app_cuenta.models import Transaccion
from django.views.generic import TemplateView, ListView

# Create your views here.


class Blank(TemplateView):
    template_name = 'blank/blank.html'


class Accounts(ListView):
    template_name = 'app_cuenta/index.html'
    model = Transaccion
    #queryset = Transaccion.objects.all()      # Metodo predefinido dentro de ListView
    #context_object_name = 'transacciones'     # Sino usa como context: 'nombredelmodelo_list'



def transaccion_new(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/accounts/')
    else:
        form = Form()

    return render(request, 'forms/forms.html', {'form': form})


