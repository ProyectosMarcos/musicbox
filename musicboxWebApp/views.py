from django.http import HttpResponse
from django.template import loader
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

def inicio(request):
    nombre_usuario = "gabo_alvarez"
    return render(request,"musicboxWebApp/INICIO.html",{"nombreUsuario":nombre_usuario})