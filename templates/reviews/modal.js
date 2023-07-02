const btnAbrirModal = 
document.querySelector("#btn-abrir-modal");
const btnAbrirModalListas = 
document.querySelector("#btn-abrir-modal-listas");



const btnCerrarModal =
document.querySelector("#btn-cerrar-modal");
const btnCerrarModalListas =
document.querySelector("#btn-cerrar-modal-listas");



const modal = 
document.querySelector("#modal");
const modalListas = 
document.querySelector("#modalListas");



btnAbrirModal.addEventListener("click",()=>{
    modal.showModal();
})
btnAbrirModalListas.addEventListener("click",()=>{
    modalListas.showModal();
})



btnCerrarModal.addEventListener("click",()=>{
    modal.close();
})
btnCerrarModalListas.addEventListener("click",()=>{
    modalListas.close();
})
