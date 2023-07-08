from django.http import HttpResponse
from django.template import loader
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from musicboxApp3.models import Album


def inicio(request):
    novedades = ["Linkin Park - Hybrid Theory","Linkin Park - Meteora","Linkin Park - Minutes to Midnight","Limp Bizkit - Chocolate Starfish And The Hot Dog Flavored Water"]
    dto_inicio = {
	    "nombreUsuario":"gabo_alvarez",
	    "novedades":novedades
    }
    return render(request,"musicboxWebApp/INICIO.html",dto_inicio)


def buscar(request):
	# REVISAR: SI SACANDO EL IF FUNCIONA NORMAL
	if request.GET["nombre_album"]:
		nombre_album=request.GET["nombre_album"]
		album = Album.objects.get(nombre=nombre_album)
		#album=articulos.objects.filter(nombre__icontains=nombre_album)
		dto_resultado_busqueda = {
			"nombre": album.nombre,
			"archivo_imagen": album.archivo_imagen
		}
		return render(request,"RESULTADO_BUSQUEDA.html",dto_resultado_busqueda)
	else:
		mensaje="No has introducido ningún dato"
		return HttpResponse(mensaje)
	

def mostrar_album(request):
	return render(request,"DETALLE_ALBUM.html")