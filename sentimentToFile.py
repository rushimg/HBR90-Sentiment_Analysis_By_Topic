import nltk, re, csv
import nltk.data
from nltk import FreqDist
from senti_classifier import senti_classifier

#topic, threshold for how many times the topic is mentioned and output file
topic = 'Financial'
threshold = 2
f = open("financial.txt", "w")

# resource csv file
data = csv.reader(open('HBR Citations_correct_abstracts.csv'))

publicationDates =[]
abstract= []
counter = 0
localMax = 0.0
localMin = 10.0
maxArticleTitle = ''
minArtilceTitle = ''
netScoreList = []


for row in data:
    counter = counter +1
    row[63] = row[63].replace(' ','')#remove whitespace
    # array of publication dates
    publicationDates.append(row[63])
   
    currentAbstract = []
    currentAbstract.append(row[123]+row[124])
    # string containing title and subjects for each term
    currentSubject = row[1]+row[71]+row[72]+row[73]+row[123]+row[124]
    #string containing current abstract and author abstract
    currentString = row[123]+row[124]
    #get frequency distribution of topic and compare to threshold
    fd = FreqDist(nltk.tokenize.word_tokenize(str.lower(currentSubject)))
    #get frequency of word
    fdTopic =  fd[str.lower(topic)]
    
    if fdTopic > threshold:
        publicationDates.append(row[63])
        print "Processing"
        #get sentiment 
        pos_score, neg_score = senti_classifier.polarity_scores(currentAbstract)
        netScore = pos_score - neg_score
        # append netScore to array
        netScoreList.append(netScore)

        print row[1]
        if netScore > localMax:
            #get title of article with max positive sentiment
            localMax = netScore
            maxArticleTitle = row[1] + row[63]+str(counter)
        if netScore < localMin:
            #get title of article with min positive sentiment
            localMin = netScore
            minArticleTitle = row[1] + row[63]+str(counter)        

#write to output file
f.write(str(netScoreList) + '\n')
f.write(str(publicationDates) + '\n')
f.write(maxArticleTitle)
f.write('\n')
f.write(minArtilceTitle)
f.close()






