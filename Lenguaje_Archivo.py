import nltk # Importar la librería nltk

# Lista de idiomas disponibles en la nltk
languages = ["spanish","english","dutch","finnish","german","italian","portuguese","turkish","danish","french","hungarian","norwegian","russian","swedish"]
# Texto a analizar
#text_to_detect = "Texto a analizar y del cual detectar el idioma en el que se encuentra"
file1 = open('convoFR.txt','r',encoding='latin-1')
text_to_detect = file1.read()
# Dividimos el texto de entrada en tokens o palabras únicas
tokens = nltk.tokenize.word_tokenize(text_to_detect)
tokens = [t.strip().lower() for t in tokens] # Convierte todos los textos a minúsculas para su posterior comparación
# Creamos un dict donde almacenaremos la cuenta de las stopwords para cada idioma
lang_count = {}
# Por cada idioma
for lang in languages:
    # Obtenemos las stopwords del idioma del módulo nltk
    stop_words = nltk.corpus.stopwords.words(lang)
    lang_count[lang] = 0 # Inicializa a 0 el contador para cada idioma
# Recorremos las palabras del texto a analizar
    for word in tokens:
        if word in stop_words: # Si la palabra se encuentra entre las stopwords, incrementa el contador
            lang_count[lang] += 1
# Obtiene el idioma con el número mayor de coincidencias
detected_language = max(lang_count, key=lang_count.get)
print (detected_language)