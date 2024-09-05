from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class FormularioVisitantes(forms.Form):
    nombre = forms.CharField(max_length=15)
    color_favorito = forms.CharField(max_length=15)

class FormularioUsuarios(forms.Form):
    nombre =forms.CharField(max_length=15)
    mail = forms.EmailField(max_length=35)
    color_favorito = forms.CharField(max_length=15)

class FormularioModeradores(forms.Form):
    nombre =forms.CharField(max_length=15)
    mail = forms.EmailField(max_length=35)
    password = forms.CharField(max_length=35)   

class Buscar(forms.Form):
    query = forms.CharField( max_length=35)

