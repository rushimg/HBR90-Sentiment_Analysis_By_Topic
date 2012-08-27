import nltk, re, csv
import nltk.data
#import itertools
from nltk import FreqDist
from senti_classifier import senti_classifier
#sentences = ['The movie was the worst movie', 'It was the worst acting by the actors']
#sentences = ["The article looks at how marketing departments can better communicate with other departments within an organization. The author suggests that the marketing department is the first and main source of knowledge about the customer but it often struggles to share its insights with the rest of the organization. Details related to research on the issue by Elliot Maltz of the University of Southern California and Ajay Kohli of the University of Texas are reviewed. Comments from Maltz are included. Issues related to the communication skills of marketing managers are discussed. The author states that content, timing and presentation are all important parts of business communication."]
#print type(sentences)
#pos_score, neg_score = senti_classifier.polarity_scores(sentences)
#netScore = pos_score - neg_score
#print netScore
#exit()


data = csv.reader(open('HBR Citations.csv'))

# get Subject term 1-5 columns

fields = data.next()
#print fields[122]
#subjectTerm! =  fields[69]
#subjectTerm1 =  fields[70 : 75]
#subjectTerm2 =  fields[71]
#subjectTerm3 =  fields[72]
#subjectTerm4 =  fields[73]
#print subjectTerm1

#prints most frequent words occording to publication date
publicationDates =[]
abstract= []
f = open("foo.txt", "w")

for row in data:
    #currentAbstract = []
    #i=i+1
    #remove whitespace
    row[63] = row[63].replace(' ','')
    publicationDates.append(row[63])
    #print row
    currentAbstract = []
    currentAbstract.append(row[122]+row[123])
    #print type(currentAbstract)
    #print currentAbstract
    #abstract.append(row[122]+row[123])# abstract and author abstract
    pos_score, neg_score = senti_classifier.polarity_scores(currentAbstract)
    netScore = pos_score - neg_score
    print netScore
    f.write(str(netScore)+'\n')
f.close()
    #print pos_score
    ##print neg_score
    #print currentAbstract
#break
#   if (netScore != 0.0):
        #print netScore
        #print currentAbstract
        #i=i+1
        #if i==5:
#break
#print publicationDates



