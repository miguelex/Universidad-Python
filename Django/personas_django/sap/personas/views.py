from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona (request, id):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'personas/detalle.html',{'persona':persona})

#PersonaForm = modelform_factory(Persona, exclude=[])

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

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        #validacion
        if formaPersona.is_valid():
            formaPersona.save() #Insertamos en BD
            return redirect('index')

    else:
        formaPersona = PersonaForm(instance =persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})