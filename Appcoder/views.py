from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Appcoder.models import Visitantes, Usuarios, Moderadores
from Appcoder.forms import FormularioVisitantes, FormularioUsuarios, FormularioModeradores

# Create your views here.
@csrf_exempt
def formularioVisitantes(req):

      if req.method == "POST":

            miFormularioVisitantes = FormularioVisitantes(req.POST) 

            print(miFormularioVisitantes)
 
            if miFormularioVisitantes.is_valid:

                  informacion = miFormularioVisitantes.cleaned_data

                  visitante = Visitantes(nombre= informacion["nombre"], color_favorito= informacion["color_favorito"])

                  visitante.save()

                  return render(req, "appcoder/busquedavisitantes.html")

      else:

            miFormularioVisitantes = FormularioVisitantes()


      return render(req, "appcoder/formulariovisitantes.html", {"miFormularioVisitantes": miFormularioVisitantes})


@csrf_exempt
def formularioUsuarios(req):

      if req.method == "POST":

            miFormularioUsuarios = FormularioUsuarios(req.POST) 

            print(miFormularioUsuarios)
 
            if miFormularioUsuarios.is_valid:

                  informacion = miFormularioUsuarios.cleaned_data

                  usuario = Usuarios(nombre= informacion["nombre"], mail= informacion["mail"], color_favorito= informacion["color_favorito"])

                  usuario.save()

                  return render(req, "appcoder/busquedavisitantes.html")

      else:

            miFormularioUsuarios = FormularioUsuarios()


      return render(req, "appcoder/formularioUsuarios.html", {"miFormularioUsuarios": miFormularioUsuarios})



@csrf_exempt
def formularioModeradores(req):

      if req.method == "POST":

            miFormularioModeradores = FormularioModeradores(req.POST) 

            print(miFormularioModeradores)
 
            if miFormularioModeradores.is_valid:

                  informacion = miFormularioModeradores.cleaned_data

                  visitante = Moderadores(nombre= informacion["nombre"],mail= informacion["mail"], password= informacion["password"])

                  visitante.save()

                  return render(req, "appcoder/busquedavisitantes.html")

      else:

            miFormularioModeradores = FormularioModeradores()


      return render(req, "appcoder/formularioModeradores.html", {"miFormularioModeradores": miFormularioModeradores})

@csrf_exempt
def busquedaVisitantes(req):
     return render(req, "appcoder/busquedaVisitantes.html")

@csrf_exempt
def buscar(req):
     
     if req.GET['nombre']:
          
          nombre = req.GET['nombre']

          color_favorito = Visitantes.objects.filter(nombre__icontains=nombre)

          return render(req, "appcoder/resultadoBusqueda.html", {"nombre": nombre, "color_favorito": color_favorito})
     
     else:
        
        respuesta = "Falta enviar datos."

        
     return HttpResponse(respuesta)

def inicio(req):
    return render(req, "appcoder/inicio.html")

def rojo(req):
    return render(req, "appcoder/rojo.html")

def azul(req):
    return render(req, "appcoder/azul.html")

def verde(req):
    return render(req, "appcoder/verde.html")

def amarillo(req):
    return render(req, "appcoder/amarillo.html")