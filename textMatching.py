'''
This file provides function for matching two texts
'''

from collections import defaultdict

import math

def getBow(text):
    text = text.lower()
    
    bowDict = defaultdict(int) # word->freq mapping dict
    wordList = text.split(' ')
    
    # print 'wordList', wordList
    
    for word in wordList:
        bowDict[word] += 1
        
    result = dict(bowDict)
    return result

def getNorm(vec):
    sum_sq = 0
    
    for x in vec:
        sum_sq += x*x
        
    norm = math.sqrt(sum_sq)
    
    return norm

def getCosineSimilarity(bow1, bow2):
    norm1 = getNorm(bow1.values())
    norm2 = getNorm(bow2.values())
    
    dot_product = 0
    
    for keyword1, freq1 in bow1.items():
        if keyword1 in bow2:
            freq2 = bow2[keyword1]
            
            dot_product += freq1*freq2
            
    cosine = float(dot_product)/(1 + float(norm1*norm2))
    
    return cosine

if __name__ == '__main__':
    print('Text matching module')
    
    text1 = 'I am data scientist'
    text2 = 'Data scientist is a great job'
    
    
    print(text1)
    print(text2)
    
    '''
    {'I':1,...}
    '''
    bow1 = getBow(text1)
    print('bow1', bow1)

    bow2 = getBow(text2)
    print('bow2', bow2)    
    
    '''
    Vocabulary
    
    i | am | data| scientist| is| a |great| job
    
    text1 = 'I am data scientist'
    text2 = 'Data scientist is a great job'
    
    text1 = [1,1,1,1,0,0,0,0]
    text2 = [0,0,1,1,1,1,1,1] - 8D
    
    cos = a.b/norm(a)*norm(b)
    '''
    
    # Find the cosine similarity between bow1 and bow2
    # s = getCosineSimilarity(bow1, bow2)
    
    print(getCosineSimilarity(bow1, bow2))
    
    