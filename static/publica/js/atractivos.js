var modal = document.getElementById("myModal");
var modalImg = document.getElementById("modal-image");
var modalDescription = document.getElementById("modal-description");

var items = document.getElementsByClassName("item");
for (var i = 0; i < items.length; i++) {
  var img = items[i].getElementsByTagName("img")[0];
  img.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src;
    modalDescription.innerHTML = this.alt;
  }
}

var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}