from django.http import HttpResponse
from django.template import loader
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def crear_lista(request):
	datos = request.POST

	usuario = Usuario.objects.get(usuario=datos["nombre_usuario"])
	

	lista_nueva = Lista()
	lista_nueva.usuario = usuario
	lista_nueva.nombre = datos["nombre_nueva_lista"]
	
	lista_nueva.descripcion = datos["descripcion_nueva_lista"]
	lista_nueva.archivo_imagen = "nose"

	lista_nueva.save()
	return listas(request,usuario.usuario)


@csrf_exempt
def incorporar_album(request):
	datos = request.POST

	lista = Lista.objects.get(nombre=datos["lista_a_incorporar"])
	album = Album.objects.get(nombre=datos["nombre_album"])

	nueva_albums_x_Lista = Albums_x_Lista()
	nueva_albums_x_Lista.lista = lista
	nueva_albums_x_Lista.album = album
	

	nueva_albums_x_Lista.save()
	return detalle_album(request,album.nombre,datos["nombre_usuario"])	


# DEFINITIVO
def login(request):
	return render(request,"musicboxWebApp/LOG_IN.html")


# DEFINITIVO
def inicio(request, nombre_usuario):
    novedades = ["Linkin Park - Hybrid Theory","Linkin Park - Meteora","Linkin Park - Minutes to Midnight","Limp Bizkit - Chocolate Starfish And The Hot Dog Flavored Water"]
    usuario = Usuario.objects.get(usuario=nombre_usuario)
    dto_inicio = {
	    "usuario": usuario,
	    "novedades":novedades
    }
    
    return render(request,"musicboxWebApp/INICIO.html",dto_inicio)


# DEFINITIVO
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
		
		return render(request,"RESULTADO_BUSQUEDA.html",dto_resultado_busqueda)
	else:
		mensaje="No has introducido ningún dato"
		return HttpResponse(mensaje)
	

# DEFINITIVO
def detalle_album(request,album,nombre_usuario): #se pasa el nombre del album
	albumObjeto = Album.objects.get(nombre=album)
	canciones = Cancion.objects.filter(album=albumObjeto)
	
	usuario = Usuario.objects.get(usuario=nombre_usuario)
	

	dto_detalle_album = {
		"usuario": usuario,
		"nombreAlbum": albumObjeto.nombre,
		"archivo_imagen": albumObjeto.archivo_imagen,
		"nombreArtista": albumObjeto.artista,
		"referencia": albumObjeto.link_referencia,
		"canciones": canciones
	}
	
	return render(request,"DETALLE_ALBUM.html",dto_detalle_album)


# DEFINITIVO
def listas(request,nombre_usuario):
	usuario = Usuario.objects.get(usuario=nombre_usuario)
	listas = Lista.objects.filter(usuario=usuario)

	dto_listas = {
		"usuario": usuario,
		"listas": listas
	}
	
	return render(request,"LISTAS.html",dto_listas)


# DEFINITIVO
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
	
	return render(request,"DETALLE_LISTA.html",dto_detalle_lista)