from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Visitantes, Usuarios, Moderadores
from Appcoder.forms import FormularioVisitantes, FormularioUsuarios, FormularioModeradores

# Create your views here.

def formularioVisitantes(request):

      if request.method == "POST":

            miFormularioVisitantes = FormularioVisitantes(request.POST) 

            print(miFormularioVisitantes)
 
            if miFormularioVisitantes.is_valid:

                  informacion = miFormularioVisitantes.cleaned_data

                  visitante = Visitantes(nombre=informacion["nombre"], color_favorito=informacion["color_favorito"])

                  visitante.save()

                  return render(request, "C:/Users/Tomás/entorno_virtual/Appcoder/templates/appcoder/inicio.html")

      else:

            miFormularioVisitantes = FormularioVisitantes()


      return render(request, "C:/Users/Tomás/entorno_virtual/Appcoder/templates/appcoder/formulariovisitantes.html", {"miFormularioVisitantes": miFormularioVisitantes})


def inicio(req):
    return render(req, "C:/Users/Tomás/entorno_virtual/Appcoder/templates/appcoder/inicio.html")

def rojo(req):
    return render(req, "C:/Users/Tomás/entorno_virtual/Appcoder/templates/appcoder/rojo.html")

def azul(req):
    return render(req, "C:/Users/Tomás/entorno_virtual/Appcoder/templates/appcoder/azul.html")

def verde(req):
    return render(req, "C:/Users/Tomás/entorno_virtual/Appcoder/templates/appcoder/verde.html")

def amarillo(req):
    return render(req, "C:/Users/Tomás/entorno_virtual/Appcoder/templates/appcoder/amarillo.html")




