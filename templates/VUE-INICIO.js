const { createApp } = Vue
createApp({
 data() {
 return {
    nombreUsuario: 'gabo_alvarez',
    cantListas: 4,
    cantAlbumesListenlist: 2,
    cantUsuariosSeguidos: 2,
    cantUsuariosSeguidores: 23,
    novedades:[
        {nombreAlbumArtista:"Linkin Park - Hybrid Theory"},
        {nombreAlbumArtista:"Linkin Park - Meteora"},
        {nombreAlbumArtista:"Linkin Park - Minutes to Midnight"},
        {nombreAlbumArtista:"Limp Bizkit - Chocolate Starfish And The Hot Dog Flavored Water"}
    ]
    }
 }
}).mount('.contenedor-grid')
