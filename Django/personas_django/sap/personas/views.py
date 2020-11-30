from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def detallePersona (request, id):
    persona = Persona.objects.get(pk=id)
    return render(request,'personas/detalle.html',{'persona':persona})
