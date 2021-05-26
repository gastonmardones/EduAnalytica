"""app_cuenta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accounts.as_view(), name='accounts'),
    path('new/', views.TransaccionCreate.as_view(), name='transaccion_new'),
    path('update/<int:pk>/', views.TransaccionUpdate.as_view(), name='transaccion_update'),
    path('delete/<int:pk>/', views.TransaccionDelete.as_view(), name='transaccion_delete'),
]
