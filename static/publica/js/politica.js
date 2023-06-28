var enlaceTerminos = document.querySelector('a.abrir-modal');
var divTerminos = document.querySelector('#terminos');
var botonCerrar = document.querySelector('.cerrar-modal');

enlaceTerminos.addEventListener('click', function(evento) {
  evento.preventDefault();
  divTerminos.style.display = 'block';
});

botonCerrar.addEventListener('click', function(evento) {
  evento.preventDefault();
  divTerminos.style.display = 'none';
});