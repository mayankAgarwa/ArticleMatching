'''
This file provides function for matching two texts
'''

from collections import defaultdict

import math

from pprint import pprint

import csv

class TextSimilarity():
    def __init__(self):
        f = open('stopwords.csv', 'r')
        reader = csv.reader(f)
        
        self.stopWordsDict = {} #stopword -> 1
        for line in reader:
            self.stopWordsDict[line[0]] = 1
            
        # pprint(self.stopWordsDict)
        
        
        f.close()
        
    def getBow(self, text):
        text = text.lower()
        
        bowDict = defaultdict(int) # word->freq mapping dict
        wordList = text.split(' ')
        
        # print 'wordList', wordList
        
        for word in wordList:
            if word not in self.stopWordsDict:
                bowDict[word] += 1
            
        result = dict(bowDict)
        return result

    def getNorm(self, vec):
        sum_sq = 0
        
        for x in vec:
            sum_sq += x*x
            
        norm = math.sqrt(sum_sq)
        
        return norm

    def getCosineSimilarity(self, bow1, bow2):
        norm1 = self.getNorm(bow1.values())
        norm2 = self.getNorm(bow2.values())
        
        dot_product = 0
        
        for keyword1, freq1 in bow1.items():
            if keyword1 in bow2:
                freq2 = bow2[keyword1]
                
                dot_product += freq1*freq2
                
        cosine = float(dot_product)/(1 + float(norm1*norm2))
        
        return cosine
    
    def getTextSimilarity(self, text1, text2):
        bow1 = self.getBow(text1)
        bow2 = self.getBow(text2)
        
        return self.getCosineSimilarity(bow1, bow2)        

    def getSimilarityBetweenTwoArticles(self, article1, article2):
        text1 = article1['headline_text']
        text2 = article2['headline_text']
        
        s = self.getTextSimilarity(text1, text2)
    
        return s
    
if __name__ == '__main__':
    print('Text matching module')
    
    text1 = 'I am data scientist'
    text2 = 'I am data'
    
    ts = TextSimilarity()
    
    print(ts.getTextSimilarity(text1, text2))

    
    