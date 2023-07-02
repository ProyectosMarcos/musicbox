const { createApp } = Vue
createApp({
 data() {
 return {
    nombreLista: "Rock de los 70s",
    descripcion: "Esta lista contiene las verdaderas canciones del rock",
    cantAlbumes:4,
    albumes:[
        {nombreAlbum: "The Wall",refAlbum:"/Proyecto-Musicbox/detalle_album/detalle_album.html",nombreArchivoAlbum:"/Proyecto-Musicbox/albums/The_Wall.png"},
        {nombreAlbum: "The Wall",refAlbum:"/Proyecto-Musicbox/detalle_album/detalle_album.html",nombreArchivoAlbum:"/Proyecto-Musicbox/albums/The_Wall.png"},
        {nombreAlbum: "The Wall",refAlbum:"/Proyecto-Musicbox/detalle_album/detalle_album.html",nombreArchivoAlbum:"/Proyecto-Musicbox/albums/The_Wall.png"},
        {nombreAlbum: "The Wall",refAlbum:"/Proyecto-Musicbox/detalle_album/detalle_album.html",nombreArchivoAlbum:"/Proyecto-Musicbox/albums/The_Wall.png"}
    ]
}
 }
}).mount('.contenedor-grid')
