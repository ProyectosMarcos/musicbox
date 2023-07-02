const usuario = document.getElementById("usuario");
const contraseña = document.getElementById("contraseña");
const formulario = document.getElementById("formulario");
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

  if (usuario.value.length < 1 || usuario.value.trim() == "") {
    mostrarMensajeError("usuario", "Nombre no valido*");
    condicion = false;
  }
  
  
  if (contraseña.value.length < 1 || contraseña.value.trim() == "") {
    mostrarMensajeError("contraseña", "Contraseña no valido*");
    condicion = false;
  }
  
  return condicion;
}

function mostrarMensajeError(claseInput, mensaje) {
  let elemento = document.querySelector(`.${claseInput}`);
  elemento.lastElementChild.innerHTML = mensaje;
}

function enviarFormulario() {
  formulario.reset();
  formulario.lastElementChild.innerHTML = "Listo!";
}