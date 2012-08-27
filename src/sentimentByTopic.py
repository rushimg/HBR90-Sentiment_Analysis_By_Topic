import nltk, re, csv
import nltk.data
#import itertools
from nltk import FreqDist
from senti_classifier import senti_classifier

#topic to change, threshold for how many times the topic is mentioned
topic = 'United'
threshold = 1

data = csv.reader(open('HBR Citations_correct_abstracts.csv'))

#fields = data.next()
#print fields[124]
#subject =  fields[71 : 75]

#prints most frequent words occording to publication date
publicationDates =[]
abstract= []
countrer = 1
counterList=[]
localMax = 0.0
localMin = 0.0
maxArticleTitle = ''
minArtilceTitle = ''
netScoreList = []

#f = open("china.txt", "w")

for row in data:
    
    row[63] = row[63].replace(' ','')#remove whitespace
    
    publicationDates.append(row[63])
   
    currentAbstract = []
    currentAbstract.append(row[123]+row[124])
    currentSubject = row[1]+row[71]+row[72]+row[73]+row[74]+row[75]
    currentString = row[123]+row[124]
    #print currentSubject
    #get frequency distribution of topic and compare to threshold
    fd = FreqDist(nltk.tokenize.word_tokenize(currentSubject))
    #print fd
    fdTopic =  fd[topic]
    
    if fdTopic > threshold:
        #print "higher than threshold"
        abstract.append(currentString)# abstract and author abstract
        pos_score, neg_score = senti_classifier.polarity_scores(currentAbstract)
        netScore = pos_score - neg_score
        #netScoreList.append(netScore)
        #counterList.append(counter)
        print "netScore:" + str(netScore)
        print row[63]
        print row[1]
        if netScore > localMax:
            #print row[0]
            localMax = netScore
            maxArticleTitle = row[1] + row[63]
        if netScore < localMin:
            localMin = netScore
            minArticleTitle = row[1] + row[63]
print maxArticleTitle
print minArtilceTitle

#f.write(str(netScore)+'\n')
#f.close()
    #break
        #print counter
     
#counter=counter+1

#else:
        #print "lower than threshold"

    
#print netScore
    #print pos_score
    ##print neg_score
    #print currentAbstract

#print publicationDates




