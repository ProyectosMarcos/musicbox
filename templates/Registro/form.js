const usuario = document.getElementById("usuario");
const correo = document.getElementById("correo");
const contraseña = document.getElementById("contraseña");
const confirmarcontraseña = document.getElementById("repeatContraseña");
const terminosYcondiciones = document.getElementById("termsAndConditions");
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
  
  if (correo.value.length < 1 || correo.value.trim() == "") {
    mostrarMensajeError("correo", "Correo no valido*");
    condicion = false;
  }
  
  if (contraseña.value.length < 1 || contraseña.value.trim() == "") {
    mostrarMensajeError("contraseña", "Contraseña no valido*");
    condicion = false;
  }
  if (confirmarcontraseña.value != contraseña.value) {
    mostrarMensajeError("repeatContraseña", "Contraseña error*");
    condicion = false;
  }
  if (!terminosYcondiciones.checked) {
    mostrarMensajeError("termsAndConditions", "Acepte*");
    condicion = false;
  } else {
    mostrarMensajeError("termsAndConditions", "");
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