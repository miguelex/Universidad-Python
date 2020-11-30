from django.forms import modelform_factory
from django.shortcuts import render, redirect

# Create your views here.
from personas.models import Persona


def detallePersona (request, id):
    persona = Persona.objects.get(pk=id)
    return render(request,'personas/detalle.html',{'persona':persona})

PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        #validacion
        if formaPersona.is_valid():
            formaPersona.save() #Insertamos en BD
            return redirect('index')

    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

