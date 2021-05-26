from django.forms import ModelForm
from app_cuenta.models import Transaccion


class TransaccionForm(ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__'
