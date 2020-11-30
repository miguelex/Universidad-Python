from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    #return HttpResponse('Hola mundo desde Django')
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()

    return render(request,'bienvenido.html', {'no_personas':no_personas, 'personas': personas})


