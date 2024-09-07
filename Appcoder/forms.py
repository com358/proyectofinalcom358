from django import forms
from Appcoder.models import Visitantes, Usuarios, Moderadores

class FormularioVisitantes(forms.ModelForm):
   class Meta:
       model = Visitantes
       fields = ['nombre', 'color_favorito'] 

class FormularioUsuarios(forms.ModelForm):
   class Meta:
       model = Usuarios
       fields = ['nombre', 'mail', 'color_favorito'] 

class FormularioModeradores(forms.ModelForm):
   class Meta:
       model = Moderadores
       fields = ['nombre', 'mail', 'password'] 

class Buscar(forms.Form):
    query = forms.CharField( max_length=35)

