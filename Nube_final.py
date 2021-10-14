from stop_words import get_stop_words
from typing import Text
import stylecloud
from stop_words import get_stop_words
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image 
import matplotlib.pyplot as plt 
import numpy as np 
import nltk
from os import remove
import cv2
from googletrans import Translator

def Limpia_Doc(nombre_Archivo):
    file1 = open(nombre_Archivo,'r',encoding='latin-1')
    linea = file1.read()
    stop_words = get_stop_words(Det_Lenguaje(file1))
    
    remove("achivo_limpio")
    palabras = linea.split()
    for r in palabras:
        if not r in stop_words:
            appendFile = open('achivo_limpio','a',encoding='latin-1')
            appendFile.write(" "+r)
            appendFile.close()

def Det_Lenguaje(file):
    languages = ["spanish","english","dutch","finnish","german","italian","portuguese","turkish","danish","french","hungarian","norwegian","russian","swedish"]
    file1 = open('achivo_limpio','r',encoding='latin-1')
    text_to_detect = file1.read()
    tokens = nltk.tokenize.word_tokenize(text_to_detect)
    tokens = [t.strip().lower() for t in tokens] # Convierte todos los textos a minúsculas para su posterior comparación
    lang_count = {}

    for lang in languages:
        stop_words = nltk.corpus.stopwords.words(lang)
        lang_count[lang] = 0 
        for word in tokens:
            if word in stop_words: 
                lang_count[lang] += 1
    detected_language = max(lang_count, key=lang_count.get)
    return detected_language

def Titulo_IMG(imagen):
    img = cv2.imread(imagen+".png")
    #Características del texto
    texto = imagen
    ubicacion = (5,50)
    font = cv2.FONT_HERSHEY_COMPLEX
    tamañoLetra = 2
    colorLetra = (255, 255, 255)
    grosorLetra = 3
    #Escribir texto
    cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
    #Guardar imagen
    cv2.imwrite(imagen+".png", img)
    #Mostrar imagen
    cv2.imshow('imagen'+".png",img)
    cv2.waitKey(0)

def Traductor(file):
    translator = Translator()
    file1 = open(file,'r',encoding='latin-1')
    linea = file1.read()
    result = translator.translate(linea,dest='es')
    #print(result.text)
    return result.text

def Nube(nombre_Archivo):
    with open('achivo_limpio','r',encoding='latin-1') as txt_file:
        texto = txt_file.read()
    nombre_Imagen="dona"
    mascara = np.array(Image.open(nombre_Imagen+".jpg"))
    wc = WordCloud(background_color='black',
    mask=mascara,
    collocations=False,
    width=800,
    height=500)
    wc.generate(texto)
    #extraer colores
    image_color = ImageColorGenerator(mascara)
    wc.recolor(color_func=image_color)
    plt.figure(figsize=(100,100))
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    wc.to_file(nombre_Archivo+".png")
    Titulo_IMG(nombre_Archivo)

def main():
    #nombre_Archivo=input("Ingresa el nombre del archivo sin extención")
    nombre_Archivo="convoIN"
    lenguaje=Det_Lenguaje(nombre_Archivo+".txt")
    #print(lenguaje !="spanish")
    if lenguaje !="spanish":
        textoT=Traductor(nombre_Archivo+".txt")
        f = open(nombre_Archivo+'T.txt','w',encoding='UTF-8')
        f.write(textoT)
        f.close()
        Limpia_Doc(nombre_Archivo+'T.txt')
        palabras_irrelevantes = get_stop_words(Det_Lenguaje('achivo_limpio'))
        Nube(nombre_Archivo+'T.txt')

    Limpia_Doc(nombre_Archivo+".txt")
    palabras_irrelevantes = get_stop_words(Det_Lenguaje('achivo_limpio'))
    Nube(nombre_Archivo)

if __name__ == '__main__':
	main()