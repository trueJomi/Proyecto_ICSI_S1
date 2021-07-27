## Views PDF tranformador

## django import
import os
from PDF_Reader.settings import BASE_DIR, MEDIA_ROOT
from django.shortcuts import redirect, render
# Create your views here.
from PDF_tranformador.forms import fileForm
from PDF_tranformador.forms import Datos
## import me
import pathlib
import fitz
import pyttsx3
from textblob import TextBlob




RUTA= pathlib.Path(BASE_DIR/'media')
RUTA_D="../media/"


def tipo_Audio(type):
    #tipo de archivo de audio
    if type == "1":
        extension=".mp3"
    elif type == "2":
        extension=".wav"
    elif type == "3":
        extension=".m4a"
    return extension

def nombreSX(name):
    name.split(".")
    return 0

def Traslate(text, idioma):
    #   Detectar idioma y traducir
    if (idioma=='Español'):
        text_temp=TextBlob(text)
        text_translate=text_temp.translate(to='es')
    elif (idioma=='Ingles'):
        text_temp=TextBlob(text)
        text_translate=text_temp.translate(to='en')
    return text_translate

def Text_for_Page(ruta):
    documento = fitz.open(ruta)
    dic_text_page={}
    pag=0
    for Pagina in documento:
        pag+=1
        text_p=Pagina.getText("text")
        tokensText=text_p.split("\n")
        textoCorregido_p=""
        for n in tokensText:
            textoCorregido_p=textoCorregido_p+n+" "
        dic_text_page[pag]=textoCorregido_p
    return dic_text_page

def Final_Text(dic_pages):
    text_final=""
    for content in dic_pages.values():
        text_final+=content
    return text_final

# def Transformar_PDF_txt(dry):
#     #Tranformar pdf varible con texto
#     documento = fitz.open(dry)
#     archivoN=dry+".txt"
#     txtcompleto=open(archivoN,"wb")
#     text_Completo=""
#     Pagina = documento.loadPage(0)
#     for Pagina in documento:
#         text=Pagina.getText("text")
#         tokensText=text.split("\n")
#         textoCorregido=""
#         for n in tokensText:
#             textoCorregido=textoCorregido+n+" "
#         text_Completo=text_Completo+textoCorregido+" "
#         textBin=textoCorregido.encode("utf8")
#         txtcompleto.write(textBin)
#         txtcompleto.write(b"--")
#     txtcompleto.close()
#     return text_Completo

def Transformar_txt_audio(txt,dry, velocidad, voz, tipo):
    #tranformar el archivo de audio
    velocidad=int(velocidad)
    voz=int(voz)
    ubicacion= dry+tipo_Audio(tipo)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("rate", velocidad)
    engine.setProperty('voice',voices[voz].id)
    engine.save_to_file(txt,ubicacion)
    engine.runAndWait()
    engine,exit
    return 0



def main(request):
    #ENlce con html
    if request.method == 'POST':
        archivo=request.FILES['archivo']
        voz=request.POST['voz']
        velocidad=request.POST['velocidad']
        tipo_dato=request.POST['tipo_dato']
        form = fileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            direc=MEDIA_ROOT+archivo.name
            paginas=Text_for_Page(direc)
            texto=Final_Text(paginas)
            # texto=Transformar_PDF_txt(direc)
            Transformar_txt_audio(texto, direc, velocidad,voz,tipo_dato)
            audio=RUTA_D+archivo.name+tipo_Audio(tipo_dato)
            os.remove(direc)
            # redirect('descarga',args={'datos':audio,})
        else:
            form = fileForm()
            audio=""
    else:
        form = fileForm()
        audio=""
    return render(
        request=request,
        template_name='pages/inicio.html',
        context={
            'form': form,
            'archivo': audio,
        }
    )

def download(requets, datos):
    return render(
        request=requets,
        template_name='pages/descarga.html',
        context={
            'archivo': datos,
        }
)