import re 
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.tokenize import word_tokenize

text = "Dalam era digital yang semakin berkembang, kebutuhan teknologi pun semakin meningkat terutama laptop yang sudah menjadi kebutuhan dalam kehidupan sehari-hari. Laptop menjadi sebuah teknologi yang cukup berperan penting dalam kebutuhan seperti bekerja, belajar, berkomunikasi, dan sebagainya. Sebagaimana halnya dengan perangkat elektronik lainnya, laptop juga seringkali memiliki berbagai permasalahan teknis. "

words = word_tokenize(text)

factory = StemmerFactory()
stemmer = factory.create_stemmer()

for w in words:
    print(w, " : ", stemmer.stem(w))

print('\n')

result = stemmer.stem(text)
print(result)
