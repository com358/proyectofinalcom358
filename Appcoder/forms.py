from django import forms

class FormularioVisitantes(forms.Form):
    nombre = forms.CharField(max_length=15)
    color_favorito = forms.CharField(max_length=15)

class FormularioUsuarios(forms.Form):
    nombre =forms.CharField(max_length=15)
    edad = forms.IntegerField
    mail = forms.EmailField(max_length=35)
    color_favorito = forms.CharField(max_length=15)

class FormularioModeradores(forms.Form):
    nombre =forms.CharField(max_length=15)
    mail = forms.EmailField(max_length=35)
    password = forms.CharField(max_length=35)   