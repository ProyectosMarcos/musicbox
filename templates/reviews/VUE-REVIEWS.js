const { createApp } = Vue
createApp({
 data() {
 return {
    nombrePagina: 'ListenList',
    cantReviews: 2,
    reviews:[
        {nombreAlbum:"Pink Floyd - Animals", nombreAlbumArchivo: "/Proyecto-Musicbox/albums/Animals.png", review:"La grabación se llevó a cabo en los estudios de la banda, Britannia Row, en Londres.", puntuacion: 2},
        {nombreAlbum:"Pink Floyd - The Wall", nombreAlbumArchivo: "/Proyecto-Musicbox/albums/The_Wall.png", review:"Escuchando el álbum conceptual en cuestión, uno tarda muy poco en descubrir la existencia del personaje principal Pink. Una persona con poca fortuna en la vida a la que le van sucediendo varios acontecimientos que van forjando su personalidad y confirmando su identidad: Pierde a su padre como consecuencia de la segunda guerra mundial, es educado por una madre estricta y cuadrada, pasa varios años en un internado lejos de todo ser querido y luego se convierte en una estrella de rock mundialmente conocida.", puntuacion: 5},
        {nombreAlbum:"Soda Stereo - Comfort y Musica para volar", nombreAlbumArchivo: "/Proyecto-Musicbox/albums/comfort.jpg", review:"Argentina ha tenido, al igual que en resto de países del mundo, grandes músicos, y es un honor poder guardar sus obras que sólo son estrellas en la galaxia de los grandes artistas de nuestra amada Tierra. No es necesario citarlos, quien aprecie la música, sabrá.", puntuacion: 5}    
    ]
     }
 }
}).mount('.contenedor-grid')