## Views PDF tranformador

## django import
from os import fsencode, remove
import os
from django.forms.widgets import Media
from django.utils import html
from PDF_Reader.settings import BASE_DIR
from django.shortcuts import redirect, render

# Create your views here.
from PDF_tranformador.forms import fileForm
from django.core.files.storage import FileSystemStorage
## import me
import pathlib
import fitz
import pyttsx3


RUTA= pathlib.Path(BASE_DIR/'media')
TYPE_AR=1
direc=''
Nombre_Archivo=''


def tipo_Audio(type,nombre):
    #tipo de archivo de audio
    if type == 1:
        nombre=nombre+".mp3"
    elif type == 2:
        nombre=nombre+".wav"
    elif type == 3:
        nombre=nombre+".m4a"
    return nombre



def Transformar_PDF_txt(dry,nombre):
    #Tranformar pdf varible con texto
    documento = fitz.open(dry)
    txtcompleto=open(RUTA/nombre+".txt","wb")
    text_Completo=""

    Pagina = documento.loadPage(0)
    for Pagina in documento:
        text=Pagina.getText("text")
        tokensText=text.split("\n")
        textoCorregido=""
        for n in tokensText:
            textoCorregido=textoCorregido+n+" "
        text_Completo=text_Completo+textoCorregido+"--"
        textBin=textoCorregido.encode("utf8")
    txtcompleto.write(textBin)
    txtcompleto.write(b"--")
    txtcompleto.close()
    return txtcompleto

def Transformar_txt_audio(txt):
    #tranformar el archivo de audio
    engine = pyttsx3.init()
    engine.setProperty("rate", 155)
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\LTTS7Jorge")
    engine.save_to_file(txt,tipo_Audio(TYPE_AR))
    engine.runAndWait()


def main(request):
    #ENlce con html
    if request.method == 'POST':
        form = fileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            gr=list(RUTA.glob('*.pdf'))
            direc=str(gr[0])
            archivo=open(direc)
            Nombre_Archivo=os.path.basename(direc)




            archivo.close()
            os.remove(direc)
    else:
        form = fileForm()
    return render(
        request=request,
        template_name='pages/inicio.html',
        context={'form':form}
    )

def download(requets):
    return render(
        request=requets,
        template_name='pages/descargar.html'
    )