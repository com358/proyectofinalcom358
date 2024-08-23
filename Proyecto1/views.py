from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from Appcoder.models import Visitantes

def saludo(request):
    return HttpResponse()

def otra_vista(request):
    return HttpResponse()


def probando_template(request):

    diccionario = {}
    mi_contexto = Context(diccionario)

    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

