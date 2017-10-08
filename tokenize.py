import nltk
import sys
from nltk.corpus import brown

print(sys.version)
print(brown.words())

sentence = "Hi. I'm testing tokenizing strings."

tokens = nltk.word_tokenize(sentence)

print(nltk.word_tokenize(sentence))
