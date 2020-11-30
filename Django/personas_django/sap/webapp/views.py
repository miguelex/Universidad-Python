from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    #return HttpResponse('Hola mundo desde Django')
    mensajes ={'msg1': 'Valor mensaje 1', 'msg2': 'Valor mensaje 2'}
    return render(request,'bienvenido.html', mensajes)

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('El telefono es 555 55 55 555<br> El email es micorreo@gmail.com')
