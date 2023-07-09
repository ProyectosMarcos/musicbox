from django.http import HttpResponse
from django.template import loader
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from musicboxApp3.models import Album,Cancion,Lista,Usuario,Albums_x_Lista


# DEFINITIVO
def iniciar(request):
	usuario_ingresado=request.GET["usuario_ingresado"]
	contrasenia_ingresado=request.GET["contrasenia_ingresado"]

	try:
		usuario_logueado = Usuario.objects.get(usuario=usuario_ingresado)
		if(usuario_logueado.contrasenia == contrasenia_ingresado):
			return inicio(request,usuario_ingresado)
		else:
			return login(request)
	except:
		return login(request)


# DEFINITIVO
def login(request):
	return render(request,"musicboxWebApp/LOG_IN.html")


def inicio(request, nombre_usuario):
    novedades = ["Linkin Park - Hybrid Theory","Linkin Park - Meteora","Linkin Park - Minutes to Midnight","Limp Bizkit - Chocolate Starfish And The Hot Dog Flavored Water"]
    usuario = Usuario.objects.get(usuario=nombre_usuario)
    dto_inicio = {
	    "usuario": usuario,
	    "novedades":novedades
    }
    print("INICIO.HTML --> " + usuario.usuario)
    return render(request,"musicboxWebApp/INICIO.html",dto_inicio)


def buscar(request):
	# REVISAR: SI SACANDO EL IF FUNCIONA NORMAL
	if request.GET["nombre_album"]:
		nombre_album=request.GET["nombre_album"]
		nombre_usuario=request.GET["nombre_usuario"]
		album = Album.objects.get(nombre=nombre_album)
		#album=articulos.objects.filter(nombre__icontains=nombre_album)

		usuario = Usuario.objects.get(usuario=nombre_usuario)

		dto_resultado_busqueda = {
			"usuario": usuario,
			"nombre": album.nombre,
			"archivo_imagen": album.archivo_imagen
		}
		print("RESULTADO_BUSQUEDA.HTML --> " + usuario.usuario)
		return render(request,"RESULTADO_BUSQUEDA.html",dto_resultado_busqueda)
	else:
		mensaje="No has introducido ningún dato"
		return HttpResponse(mensaje)
	

def detalle_album(request,album,nombre_usuario): #se pasa el nombre del album
	albumObjeto = Album.objects.get(nombre=album)
	canciones = Cancion.objects.filter(album=albumObjeto)
	
	usuario = Usuario.objects.get(usuario=nombre_usuario)
	print("HARDCODEADO")

	dto_detalle_album = {
		"usuario": usuario,
		"nombreAlbum": albumObjeto.nombre,
		"archivo_imagen": albumObjeto.archivo_imagen,
		"nombreArtista": albumObjeto.artista,
		"referencia": albumObjeto.link_referencia,
		"canciones": canciones
	}
	print("DETALLE_ALBUM.HTML --> " + usuario.usuario)
	return render(request,"DETALLE_ALBUM.html",dto_detalle_album)


def listas(request,nombre_usuario): # id_usuario string ?
	usuario = Usuario.objects.get(usuario=nombre_usuario)
	listas = Lista.objects.filter(usuario=usuario)

	dto_listas = {
		"usuario": usuario,
		"listas": listas
	}
	print("LISTAS.HTML --> " + usuario.usuario)
	return render(request,"LISTAS.html",dto_listas)


def detalle_lista(request,lista_nombre,nombre_usuario):
	lista_nombre_aux = lista_nombre.split("+")
	lista_nombre_limpia = " ".join(lista_nombre_aux)
	
	lista = Lista.objects.get(nombre=lista_nombre_limpia)

	# traer todos los albums_x_lista que contengan como FK a lista
	listado_albums_x_lista = Albums_x_Lista.objects.filter(lista=lista)
	albums = [] 

	for albums_x_lista in listado_albums_x_lista:
		album = albums_x_lista.album
		albums.append(album)
	
	usuario = Usuario.objects.get(usuario=nombre_usuario)

	dto_detalle_lista = {
		"usuario": usuario,
		"nombreLista":lista.nombre,
		"descripcion":lista.descripcion,
		"albums": albums
	}
	print("DETALLE_LISTA.HTML --> " + usuario.usuario)
	return render(request,"DETALLE_LISTA.html",dto_detalle_lista)