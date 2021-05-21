from django.forms import ModelForm
from app_cuenta.models import Transaccion


class Form(ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__'
