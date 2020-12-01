from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


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

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if persona:
        persona.delete()
    return redirect('index')

def detalleDomicilio (request, id):
    domicilio = get_object_or_404(Domicilio,pk=id)
    return render(request,'domicilios/detalle.html',{'domicilio':domicilio})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        #validacion
        if formaDomicilio.is_valid():
            formaDomicilio.save() #Insertamos en BD
            return redirect('domicilios')

    else:
        formaDomicilio = DomicilioForm()

    return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})

def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        #validacion
        if formaDomicilio.is_valid():
            formaDomicilio.save() #Insertamos en BD
            return redirect('domicilios')

    else:
        formaDomicilio = DomicilioForm(instance = domicilio)

    return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})

def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)

    if domicilio:
        domicilio.delete()
    return redirect('domicilios')
