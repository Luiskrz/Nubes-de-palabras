from typing import Text
import stylecloud
from stop_words import get_stop_words
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image #carga imagen
import matplotlib.pyplot as plt #grafica la imagen
import numpy as np #

'''
palabras_irrelevantes = get_stop_words('spanish')
stylecloud.gen_stylecloud(file_path="materia.txt",
icon_name='fas fa-fish',
#colors='white',
palette='scientific.sequential.Bamako_11',
background_color='black',
output_name='salida.png',
custom_stopwords=palabras_irrelevantes)
'''

#graficar la nube de palabras
mascara = np.array(Image.open('horda.jpg'))
wc = WordCloud(background_color='white',
mask=mascara,
collocations=False,
width=600,
height=300)
palabras_irrelevantes = get_stop_words('spanish')
with open('materia_limpio','r',encoding='UTF8') as txt_file:
    texto = txt_file.read()

wc.generate(texto)

#extraer colores
image_color = ImageColorGenerator(mascara)
wc.recolor(color_func=image_color)
plt.figure(figsize=(20,10))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
wc.to_file('nube.png')
plt.show()