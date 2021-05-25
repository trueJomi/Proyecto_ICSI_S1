#   Vsita del La pagina principal

# Django
from os import error
from django.shortcuts import render

# Programas
import fitz
import pyttsx3


Ruta="C:\ "
type_archivo=1

def Nombre_Archivo(Directorio):
    ##estraes el nombre del archivo junto a su extension
    D_Archivo= Directorio.split("/")        
    nombre_archivo=D_Archivo[(len(D_Archivo)-1)]
    return nombre_archivo

def tipo_Audio(type):
    #tipo de archivo de audio
    nombre=Nombre_Archivo(Ruta)
    if type == 1:
        nombre=nombre+".mp3"
    elif type == 2:
        nombre=nombre+".wav"
    elif type == 3:
        nombre=nombre+".m4a"
    return nombre



def Transformar_PDF_txt():
    #Tranformar pdf varible con texto
    documento = fitz.open(Ruta)
    nombre_archivo=Nombre_Archivo(Ruta)
    txtcompleto=open(nombre_archivo+".txt","wb")
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

def Transformar_txt_audio(txt,):
    engine = pyttsx3.init()
    engine.setProperty("rate", 155)
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\LTTS7Jorge")
    engine.save_to_file(txt,tipo_Audio(type_archivo))
    engine.runAndWait()


def main(request):
    #ENlce con html

    if request.method =="POST":
        print("*"*10)
        Directorio = request.POST['Ruta']
        print(Directorio)
        print("*"*10)
    return render(request,'index.html')