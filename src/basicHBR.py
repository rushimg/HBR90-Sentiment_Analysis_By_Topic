import nltk, re, csv
import nltk.data
import itertools
from nltk import FreqDist

## load from text file
#raw = open('HBR Citations.csv', 'r').read()
data = csv.reader(open('HBR Citations.csv'))

# get Subject term 1-5 columns
fields = data.next()
#subjectTerm! =  fields[69]
subjectTerm1 =  fields[70 : 75]
#subjectTerm2 =  fields[71]
#subjectTerm3 =  fields[72]
#subjectTerm4 =  fields[73]
#print subjectTerm1

#prints most frequent words occording to publication date
publicationDates =[]
fequentWords =[]
for row in data:
    publicationDates.append(row[63])
    #print row
    fd = FreqDist(row)
    fequentWords.append(fd.keys()[3])

#print publicationDates
print fequentWords

#sentences = "Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world."

##Convert to word array and in NLTK format
#tagged = nltk.tokenize.word_tokenize(raw)
#tagged2 = nltk.sent_tokenize(sentences.strip())
#tagged2 = [nltk.word_tokenize(sent) for sent in tagged2]
#tagged2 = [nltk.pos_tag(sent) for sent in tagged2]
#print tagged2

# find most frequent words throughout article
#fd = FreqDist(tagged)
#print fd.keys()[:10]

# then find/choose common words (i.e. big three, wall street, government, wall)

# run sentiment analysis of these versus time of publication

# graph


