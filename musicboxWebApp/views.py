from django.http import HttpResponse
from django.template import loader
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from musicboxApp3.models import Album,Cancion,Lista,Usuario


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
	

def detalle_album(request,album): #se pasa el nombre del album
	albumObjeto = Album.objects.get(nombre=album)
	canciones = Cancion.objects.filter(album=albumObjeto)
	
	dto_detalle_album = {
		"nombreAlbum": albumObjeto.nombre,
		"archivo_imagen": albumObjeto.archivo_imagen,
		"nombreArtista": albumObjeto.artista,
		"referencia": albumObjeto.link_referencia,
		"canciones": canciones
	}
	return render(request,"DETALLE_ALBUM.html",dto_detalle_album)


def listas(request,nombre_usuario): # id_usuario string ?
	usuario = Usuario.objects.get(usuario=nombre_usuario)
	listas = Lista.objects.filter(usuario=usuario)

	dto_listas = {
		"usuario": usuario,
		"listas": listas
	}
	
	return render(request,"LISTAS.html",dto_listas)