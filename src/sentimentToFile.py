import nltk, re, csv
import nltk.data
#import itertools
from nltk import FreqDist
from senti_classifier import senti_classifier

#topic to change, threshold for how many times the topic is mentioned
topic = 'Financial'
threshold = 2
f = open("financial.txt", "w")

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
    counter = counter +1
    #row[63] = row[63].replace(' ','')#remove whitespace
    
    #publicationDates.append(row[63])
   
    currentAbstract = []
    currentAbstract.append(row[123]+row[124])
    currentSubject = row[1]+row[71]+row[72]+row[73]+row[123]+row[124]
    currentString = row[123]+row[124]
    #print currentSubject
    #get frequency distribution of topic and compare to threshold
    fd = FreqDist(nltk.tokenize.word_tokenize(str.lower(currentSubject)))
    #print fd
    fdTopic =  fd[str.lower(topic)]
    
    if fdTopic > threshold:
        # counter = counter +1
        publicationDates.append(row[63])
        print "Processing"
        #abstract.append(currentString)# abstract and author abstract
        pos_score, neg_score = senti_classifier.polarity_scores(currentAbstract)
        netScore = pos_score - neg_score
        netScoreList.append(netScore)
        counterList.append(counter)
        #print "netScore:" + str(netScore)
        #print row[63]
        print row[1]
        if netScore > localMax:
            localMax = netScore
            maxArticleTitle = row[1] + row[63]+str(counter)
        if netScore < localMin:
            localMin = netScore
            minArticleTitle = row[1] + row[63]+str(counter)        
print "Almost Done"
#print maxArticleTitle
#print minArtilceTitle

f.write(str(netScoreList) + '\n')
f.write(str(counterList) + '\n')
f.write(str(publicationDates) + '\n')
f.write(maxArticleTitle)
f.write('\n')
f.write(minArtilceTitle)
f.close()






