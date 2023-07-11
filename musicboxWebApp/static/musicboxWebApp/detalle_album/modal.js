const btnAbrirModalListas = document.querySelector("#btn-abrir-modal-listas");
const modalListas = document.querySelector("#modalListas");
// const btnCerrarModalListas = document.querySelector("#btn-cerrar-modal-listas");

btnAbrirModalListas.addEventListener("click",()=>{
    modalListas.showModal();
})

/*
btnCerrarModalListas.addEventListener("click",()=>{
    modalListas.close();
}) */

function cerrarModal(event) {
    event.stopPropagation();
    event.preventDefault();
    modal.close();
}