from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

print("\n")
#file = open("D://Downloads/V Extras/webmining_lab1.txt", "r")
#text = file.read()
text = input("Enter the text: ")

stop_words=['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']
token = word_tokenize(text)
filtered_sentences=[]
for w in token:
    if w not in stop_words:
        filtered_sentences.append(w)
print("\nBefore removing stop words: ")
print(token)
print("\nAfter removing stop words: ")
print(filtered_sentences)