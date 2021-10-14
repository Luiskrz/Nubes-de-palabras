
from stop_words import get_stop_words
#from nltk.tokenize import word_tokenize
 
# word_tokenize accepts
# a string as an input, not a file.
stop_words = get_stop_words('spanish')
file1 = open('materia.txt','r',encoding='UTF8')
 
# Use this to read file content as a stream:
line = file1.read()

words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('materia_limpio','a',encoding='UTF-8')
        appendFile.write(" "+r)
        appendFile.close() 