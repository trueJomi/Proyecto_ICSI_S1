## Views PDF tranformador

## django import
import os
from PDF_Reader.settings import BASE_DIR
from django.shortcuts import redirect, render
# Create your views here.
from PDF_tranformador.forms import fileForm
## import me
import pathlib
import fitz
import pyttsx3



RUTA= pathlib.Path(BASE_DIR/'media')
tipo=1
RUTA_D="../media/"


def obtener_nombre(root):
    nombre=os.path.basename(root)
    NTemp=nombre.split(".")
    nombre=NTemp[0]
    return nombre

def tipo_Audio(type):
    #tipo de archivo de audio
    if type == 1:
        extension=".mp3"
    elif type == 2:
        extension=".wav"
    elif type == 3:
        extension=".m4a"
    return extension



def Transformar_PDF_txt(dry):
    #Tranformar pdf varible con texto
    documento = fitz.open(dry)
    archivoN=obtener_nombre(dry)+".txt"
    txtcompleto=open(archivoN,"wb")
    text_Completo=""
    Pagina = documento.loadPage(0)
    for Pagina in documento:
        text=Pagina.getText("text")
        tokensText=text.split("\n")
        textoCorregido=""
        for n in tokensText:
            textoCorregido=textoCorregido+n+" "
        text_Completo=text_Completo+textoCorregido+" "
        textBin=textoCorregido.encode("utf8")
        txtcompleto.write(textBin)
        txtcompleto.write(b"--")
    txtcompleto.close()
    return text_Completo

def Transformar_txt_audio(txt,dry):
    #tranformar el archivo de audio
    ubicacion= obtener_nombre(dry)+tipo_Audio(tipo)
    engine = pyttsx3.init()
    engine.setProperty("rate", 155)
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\LTTS7Jorge")
    engine.save_to_file(txt,ubicacion)
    engine.runAndWait()



def main(request):
    #ENlce con html
    if request.method == 'POST':
        form = fileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            gr=list(RUTA.glob('*.pdf'))
            direc=str(gr[0])
            texto=Transformar_PDF_txt(direc)
            Transformar_txt_audio(texto, direc)
            # os.remove(direc)
            return redirect('descarga')
        else:
            form = fileForm()
    else:
        form = fileForm()
    return render(
        request=request,
        template_name='pages/inicio.html',
        context={
            'form': form,
        }
    )

def download(requets):
    gr=list(RUTA.glob('*'+tipo_Audio(tipo)))
    print(gr)
    direc=str(gr[0])
    audio=RUTA_D+obtener_nombre(direc)+tipo_Audio(tipo)
    print(audio)
    return render(
        request=requets,
        template_name='pages/download.html',
        context={
            'archivo':audio,
        }
)