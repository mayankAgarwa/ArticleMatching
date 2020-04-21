'''
This module provides functions to find matching articles to a given article
'''

from textMatching import getCosineSimilarity, getBow

import csv

from pprint import pprint

import time

from getSimilarityBetweenTexts import TextSimilarity

import json

def getTopArticles(article):
    similarityExcelSheet = []
    for articleid2, article2 in articleIdToArticleMapping.items():
        # s = getSimilarityBetweenTwoArticleIds(articleid1, articleid2, articleIdToArticleMapping)
        
        if articleid == articleid2:
            continue

        s = ts.getSimilarityBetweenTwoArticles(article, article2)
        
        if s > 0.7: #min cosine
            row = [articleid, articleid2, s]
        
            # print row
            similarityExcelSheet.append(row)
        
    
    
    #Get topN
    topN = 5
    sortedSimilaritySheet = sorted(similarityExcelSheet, key = lambda x: x[2], reverse = True)
    topNExcelSheet = sortedSimilaritySheet[0:topN]
    # print 'topNExcelSheet:', topNExcelSheet
    
    article2bsent = []
    for (article_orig, article_id2, similarity) in topNExcelSheet:
        article2bsent.append(article_id2)

    # pprint(article2bsent)
    
    return article2bsent

def getTextSimilarity(text1, text2):
    similarity = ts.getTextSimilarity(text1, text2)
    return similarity

def getSimilarityBetweenTwoArticles(article1, article2):
    text1 = article1['headline_text']
    text2 = article2['headline_text']
    
    s = getTextSimilarity(text1, text2)

    return s

if __name__ == '__main__':
    print('Compute Article Similarity and Save Model')
    
    # Load the dataset
        
    f = open('data.csv', 'r')
    fieldnames = ['id', 'publish_date', 'headline_category', 'headline_text']
    reader = csv.DictReader(f, fieldnames=fieldnames)
    
    
    # Create the text similarity object
    ts = TextSimilarity()
        
    
    i = 0
    articleIdToArticleMapping = {} #id->article
    st_time = time.time()
    for article in reader:
        if i % 100 == 0:
            print (i, ' articles read in ', time.time() - st_time, ' seconds')
        if i == 0:
            # skip the header
            i += 1
            continue
        
        
        text = article['headline_text']        
        id = article['id']
        
        articleIdToArticleMapping[id] = article
        
        
        if i > 10:
            break
        
        i += 1
        
    
    # pprint(articleIdToArticleMapping)
    
    
    print('=================================')
    
    articlesToBeSentMapping = {} #article-> which article to send
    i = 0
    for articleid, article in articleIdToArticleMapping.items():
        s = getTopArticles(article)
        
        articlesToBeSentMapping[articleid] = s

        if i % 100 == 0:        
            print('Similarity Computation ', i, ' in ', time.time() - st_time, ' seconds')
        # print [articleid, s]
        
        i += 1
    
    
    # pprint({'articlesToBeSentMapping': articlesToBeSentMapping})

    
    for articleid, article in articleIdToArticleMapping.items(): 
        if len(articlesToBeSentMapping[articleid]) > 0:
            print('Original Article:', articleIdToArticleMapping[articleid]['headline_text'],'\t',articleid)
        
            print('\t Matching Articles:')
                  
        for articleid in articlesToBeSentMapping[articleid]:

                print('\t \t', articleIdToArticleMapping[articleid]['headline_text'],'\t ',articleid)

    
    f.close()
    
    
    # Save the model to a json
    g = open('articlesToBeSentMapping.json', 'w')
    json.dump(articlesToBeSentMapping, g)
    g.close()


    # Save the article id to article mapping to a json
    g = open('articleIdToArticleMapping.json', 'w')
    json.dump(articleIdToArticleMapping, g)
    g.close()    
    

     