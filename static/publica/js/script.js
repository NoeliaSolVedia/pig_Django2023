// Cuando el usuario hace scroll ejecuto myFuncion
window.onscroll = function() {myFunction()};

var secciones = document.getElementsByTagName("section");
var meses = document.getElementsByClassName("mes");

function myFunction(){
  if (window.pageYOffset >= secciones[0].offsetTop) {
    eliminarClase();
  }
  if (window.pageYOffset >= secciones[1].offsetTop - 100) {
    eliminarClase();
    meses[0].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[2].offsetTop - 100) {
    eliminarClase();
    meses[1].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[3].offsetTop - 100) {
    eliminarClase();
    meses[2].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[4].offsetTop - 100) {
    eliminarClase();
    meses[3].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[5].offsetTop - 100) {
    eliminarClase();
    meses[4].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[6].offsetTop - 100) {
    eliminarClase();
    meses[5].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[7].offsetTop -100) {
    eliminarClase();
    meses[6].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[8].offsetTop -100) {
    eliminarClase();
    meses[7].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[9].offsetTop -100) {
    eliminarClase();
    meses[8].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[10].offsetTop -100) {
    eliminarClase();
    meses[9].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[11].offsetTop -100) {
    eliminarClase();
    meses[10].classList.add("seleccionado");
  }
  if (window.pageYOffset >= secciones[12].offsetTop -100) {
    eliminarClase();
    meses[11].classList.add("seleccionado");
  }
  
}

function eliminarClase(){
  for(i=0; i < meses.length;i++){
    meses[i].classList.remove("seleccionado");
    }
}