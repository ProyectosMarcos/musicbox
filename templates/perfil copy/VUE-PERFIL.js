const { createApp } = Vue
createApp({
 data() {
 return {
    nombreUsuario: 'gabo_alvarez',
    avatar: "/Proyecto-Musicbox/iconos/zeppelin.jpg",
    passwordActual:"hola",
    cantArtistasFavoritos: 1,
    cantAlbumesFavoritos: 1,
    cantActividadReciente: 1,
    loSigo:0, // 1: SI, 0: NO
    artistasFavoritos:[
        {nombre:"the_beatles",nombreArtistaArchivo:"/Proyecto-Musicbox/perfil/album-modificado/The Beatles.png"},
        {nombre:"the_beatles",nombreArtistaArchivo:"/Proyecto-Musicbox/perfil/album-modificado/The Beatles.png"},
        {nombre:"the_beatles",nombreArtistaArchivo:"/Proyecto-Musicbox/perfil/album-modificado/The Beatles.png"},
        {nombre:"the_beatles",nombreArtistaArchivo:"/Proyecto-Musicbox/perfil/album-modificado/The Beatles.png"},
        {nombre:"the_beatles",nombreArtistaArchivo:"/Proyecto-Musicbox/perfil/album-modificado/The Beatles.png"}
    ],
    albumesFavoritos:[
        {nombre:"The Dark Side of The Moon1",nombreAlbumArchivo:"/Proyecto-Musicbox/albums/triangulo.png"},
        {nombre:"The Dark Side of The Moon2",nombreAlbumArchivo:"/Proyecto-Musicbox/albums/triangulo.png"},
        {nombre:"The Dark Side of The Moon3",nombreAlbumArchivo:"/Proyecto-Musicbox/albums/triangulo.png"},
        {nombre:"The Dark Side of The Moon4",nombreAlbumArchivo:"/Proyecto-Musicbox/albums/triangulo.png"},
        {nombre:"The Dark Side of The Moon5",nombreAlbumArchivo:"/Proyecto-Musicbox/albums/triangulo.png"}
    ],
    actividadReciente:[
        {nombre:"Playlist",nombreAlbumArchivo:"/Proyecto-Musicbox/iconos/album-de-musica.png"},
        {nombre:"Playlist",nombreAlbumArchivo:"/Proyecto-Musicbox/iconos/album-de-musica.png"},
        {nombre:"Playlist",nombreAlbumArchivo:"/Proyecto-Musicbox/iconos/album-de-musica.png"},
        {nombre:"Playlist",nombreAlbumArchivo:"/Proyecto-Musicbox/iconos/album-de-musica.png"},
        {nombre:"Playlist",nombreAlbumArchivo:"/Proyecto-Musicbox/iconos/album-de-musica.png"}
    ]
    }
 }
}).mount('.contenedor-grid')
