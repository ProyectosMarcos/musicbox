from django.contrib import admin
from musicboxApp3.models import Usuario,Album,Cancion,Lista,Albums_x_Lista 

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("usuario","contrasenia","email","archivo_imagen") 

class AlbumAdmin(admin.ModelAdmin):
    list_display=("artista","nombre","link_referencia","archivo_imagen")  

class CancionAdmin(admin.ModelAdmin):
    list_display=("album","nombre")

class ListaAdmin(admin.ModelAdmin):
    list_display=("usuario","nombre","descripcion","archivo_imagen")  

class Albums_x_ListaAdmin(admin.ModelAdmin):
    list_display=("lista","album")


admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Cancion,CancionAdmin)
admin.site.register(Lista,ListaAdmin)
admin.site.register(Albums_x_Lista,Albums_x_ListaAdmin)