import nltk, re, csv
import nltk.data
#import itertools
from nltk import FreqDist
from senti_classifier import senti_classifier

max = '1-Mar-97'
topic = 'American'
data = csv.reader(open('HBR Citations_correct_abstracts.csv'))

#prints most frequent words occording to publication date
publicationDates =[]
abstract= []
counter = 0
counterList=[]
localMax = 0.0
localMin = 10.0
maxArticleTitle = ''
minArtilceTitle = ''
netScoreList = []



for row in data:
    

    
 
    
    if row[63] == max:
        print "processing"
        currentSubject = row[1]+row[71]+row[72]+row[73]+row[123]+row[124]
        
        fd = FreqDist(nltk.tokenize.word_tokenize(str.lower(currentSubject)))
        fdTopic =  fd[str.lower(topic)]

        if fdTopic > 2:
            print "max " + row[1]
    








