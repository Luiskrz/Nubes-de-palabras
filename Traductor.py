#pip install googletrans==3.1.0a0
from googletrans import Translator

translator = Translator()
file1 = open("convoIN.txt",'r',encoding='latin-1')
linea = file1.read()
result = translator.translate(linea,dest='es')
print(result.text)
