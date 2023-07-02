const { createApp } = Vue
createApp({
 data() {
 return {
    nombrePagina: 'ListenList',
    cantAlbumesPendientes: 4,
    albumes:[
        {nombreAlbum:"Animals", nombreAlbumArchivo: "/Proyecto-Musicbox/albums/Animals.png"},
        {nombreAlbum:"The Wall", nombreAlbumArchivo: "/Proyecto-Musicbox/albums/The_Wall.png"},
        {nombreAlbum:"Comfort y musica para volar", nombreAlbumArchivo: "/Proyecto-Musicbox/albums/comfort.jpg"},
        {nombreAlbum:"30", nombreAlbumArchivo: "/Proyecto-Musicbox/albums/adele.png"}
    ]
     }
 }
}).mount('.contenedor-grid')
