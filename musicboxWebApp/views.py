from django.http import HttpResponse
from django.template import loader
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render


def inicio(request):
    novedades = ["Linkin Park - Hybrid Theory","Linkin Park - Meteora","Linkin Park - Minutes to Midnight","Limp Bizkit - Chocolate Starfish And The Hot Dog Flavored Water"]
    dto_inicio = {
	    "nombreUsuario":"gabo_alvarez",
	    "cantListas":1,
	    "cantAlbumesListenlist":2,
	    "cantUsuariosSeguidos":3,
	    "cantUsuariosSeguidores":4,
	    "novedades":novedades
    }

    return render(request,"musicboxWebApp/INICIO.html",dto_inicio)