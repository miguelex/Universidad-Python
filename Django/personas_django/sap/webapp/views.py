from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('El telefono es 555 55 55 555<br> El email es micorreo@gmail.com')
