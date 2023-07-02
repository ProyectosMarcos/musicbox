const { createApp } = Vue
createApp({
 data() {
 return {
    nombreAlbum: 'Animals',
    nombreArtista: 'Pink Floyd',
    anio: 1977,
    duracion: 42,
    nombreAlbumArchivo: "/Proyecto-Musicbox/albums/Animals.png",
    canciones: [
        {nombreCancion: "Pigs on the Wing 1"},
        {nombreCancion: "Dogs"},
        {nombreCancion: "Pigs (Three Different Ones)"},
        {nombreCancion: "Sheep"},
        {nombreCancion: "Pigs on the Wing 2"},
    ],
    linkInfo: "https://es.wikipedia.org/wiki/Animals_(%C3%A1lbum)",
    reviews:[
        {usuario: "gabo_alvarez",puntaje: 4,review:"La selección argentina sub 20 empieza a calentar motores para lo que será su debut estelar en el Mundial de la categoría que se desarrollará en el país. El Estadio Único Madre de Ciudades será el epicentro de la acción desde las 18 para los dirigidos por Javier Mascherano, quienes a horas del cruce ante Uzbekistán posaron frente a las cámaras de FIFA para las imágenes protocolares de la competencia."},
        {usuario: "marcos_music",puntaje: 3,review:"Excelente portada."}
    ],
    listas:[
        {nombreLista: "Rock 70s", check: 1},
        {nombreLista: "Rock 60s", check: 0},
        {nombreLista: "Rock 80s", check: 1},
        {nombreLista: "Rock 90s", check: 0}
    ]
    }
 }
}).mount('.contenedor-grid')
