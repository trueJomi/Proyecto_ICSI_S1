document.getElementById('boton').addEventListener('click', openDialog);
document.getElementById('cargar').addEventListener('click',loading)

function openDialog() {
  document.getElementById('fileid').click();
}

function loading(){
  document.getElementById("loader").style.visibility="visible";
}

