document.getElementById('boton').addEventListener('click', openDialog);
document.getElementById('cargar').addEventListener('click',loading)
document.getElementById('fileid').addEventListener('change',submit)

function openDialog() {
  document.getElementById('fileid').click();
}

function loading(){
  document.getElementById("loader").style.visibility="visible";
}

function submit(){
  document.getElementById("cargar").style.visibility="visible";
  document.getElementById("cargar").style.position="relative";
}