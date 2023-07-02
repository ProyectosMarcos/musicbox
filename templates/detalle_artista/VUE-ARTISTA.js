const { createApp } = Vue
createApp({
 data() {
 return {
    esFav:0,
    nombre:"Freddie Mercury",
    imagen:"/Proyecto-Musicbox/albums/Animals.png",
    biografia: "Freddie Mercury (nacido como Farrokh Bulsara;Stone Town, Ciudad de Zanzíbar, actual Tanzania, 5 de septiembre de 1946-Kensington, Londres, 24 de noviembre de 1991) fue un cantante y compositor británico que alcanzó fama mundial por ser el vocalista principal y pianista de la banda de rock Queen. Siendo intérprete, ha sido reconocido por su poderosa voz y extravagantes puestas en escena.4​5​6​ Como compositor, escribió muchos de los éxitos de Queen, tales como «Killer Queen», «Bohemian Rhapsody», «Somebody to Love», «We Are the Champions», «Don't Stop Me Now», «Crazy Little Thing Called Love», «It's a Hard Life» o «Innuendo». Además de la actividad con la banda, en los años ochenta lanzó su carrera como solista que lo llevó a publicar dos álbumes: Mr. Bad Guy (1985) y Barcelona (1988), este último en colaboración con la soprano española Montserrat Caballé. El sencillo homónimo, una colaboración entre ambos, fue la canción oficial de los Juegos Olímpicos de Barcelona 1992.7​Falleció por una bronconeumonía, derivada de complicaciones del sida, el 24 de noviembre de 1991, un día después de comunicar oficialmente que padecía esta enfermedad. En 2006, la revista Time Asia lo nombró como uno de los héroes asiáticos más influyentes de los últimos sesenta años.8​ En 2005, en una encuesta organizada por Blender y MTV2, fue nombrado el mejor cantante masculino de todos los tiempos.9​ En 2008, la revista estadounidense Rolling Stone lo colocó en el puesto 18 en su lista de los cien mejores cantantes de todos los tiempos.10​5​ Mientras que Classic Rock, al año siguiente, lo consideró el mejor cantante de rock de la historia.11​ Por su parte, Allmusic definió a Mercury como «uno de los líderes más carismáticos y dinámicos en la historia del rock».",
    albumes:["Mr. Bad Guy","Barcelona"],
    ref:"https://es.wikipedia.org/wiki/Animals_(%C3%A1lbum)"
    }
 }
}).mount('.contenedor-grid')
