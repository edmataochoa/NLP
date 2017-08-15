import nltk
from nltk.corpus import brown

print(brown.words())

sentence = "Who are you, anyway?"

tokens = nltk.word_tokenize(sentence)

print(nltk.word_tokenize(sentence))

for word in tokens:
    if word.isalpha():
        print(word)
