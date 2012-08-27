import nltk
import nltk.data
from nltk import FreqDist

#prints top 1000 most frequent words and the frequency of the string 'Economics'

## load from text file
raw = open('HBR Citations_correct_abstracts.csv', 'r').read()

#sentences = "Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world."

##Convert to word array and in NLTK format
tagged = nltk.tokenize.word_tokenize(raw)

# find most frequent words throughout article
fd = FreqDist(tagged)
#print fd.keys()[:1000]
print fd['Washington']
print fd['China']
print fd['Technology']
print fd['Manufacturing']
print fd['Innovation']

