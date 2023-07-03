const buscarTexto = document.getElementById("buscarTexto");
const selector = document.getElementById("selectorOption");
const formulario = document.getElementById("formulario-1");
const listInputs = document.querySelectorAll(".form-input");

formulario.addEventListener("submit", (e) => {
  e.preventDefault();
  let condicion = validacionForm();
  if (condicion) {
    enviarFormulario();
  }
});

 function validacionForm() {
  formulario.lastElementChild.innerHTML = "";
  let condicion = true;
  listInputs.forEach((element) => {
     element.lastElementChild.innerHTML = "";
  });

//   if (buscarTexto.value.length < 1 || buscarTexto.value.trim() == "") {
//     mostrarMensajeError("buscarTexto", "Nombre no valido*");
//     condicion = false;
//   }
  
  
//   // if (selector.value.length < 1 || selector.value.trim() == "") {
//   //   mostrarMensajeError("selectorOption", "Contraseña no valido*");
//   //   condicion = false;
//   // }

 
//   return condicion;
// }

function mostrarMensajeError(claseInput, mensaje) {
  let elemento = document.querySelector(`.${claseInput}`);
  elemento.lastElementChild.innerHTML = mensaje;
 }


function enviarFormulario() {
  formulario.reset();
 formulario.lastElementChild.innerHTML = "Listo!";
 }
 }
function validarSelectorBusqueda() {
  let validarSelectorBusqueda=document.getElementById('selectorOption')
  if (validarSelectorBusqueda.value==0 || 
    validarSelectorBusqueda.value=="")
    {
      alert ("Selecciona una opcion para poder continuar")
      validarSelectorBusqueda.focus();
    }else
    alert ("Opcion seleccionada con exito")
    validarSelectorBusqueda.focus();
  }