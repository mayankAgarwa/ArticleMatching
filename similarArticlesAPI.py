from flask import Flask
app = Flask(__name__)

import json

# Load our model
f = open('articlesToBeSentMapping.json', 'rb')
articlesToBeSentMapping = json.load(f)
f.close()


f = open('articleIdToArticleMapping.json', 'rb')
articleIdToArticleMapping = json.load(f)
f.close()

@app.route("/runMeAgain")
def runMeAgain():
    # Load our model
    f = open('articlesToBeSentMapping.json', 'rb')
    articlesToBeSentMapping = json.load(f)
    f.close()
    
    
    f = open('articleIdToArticleMapping.json', 'rb')
    articleIdToArticleMapping = json.load(f)
    f.close()
    
@app.route("/hello")
def hello():
    return "Hello Prashant!"


@app.route("/<article_id>")
def getSimilarArticles(article_id):
    displayString = ''

    
    # Grab the original article
    original_article = articleIdToArticleMapping[article_id]['headline_text']
    
    # Add it to the display string
    
    
    displayString += '''
    <b>Orignial Article</b> <br/>

    ''' + original_article + '<br/>'
    
    # Get matching article ids as a list
    matchingArticleIds = articlesToBeSentMapping[article_id]
    
    # Add them comma seperated to the display string
    displayString += '<br/><b>Matching article ids:</b>' + ','.join(matchingArticleIds) + '<br/><br/>'
    
    # print matchingArticleIds
    
    displayString +=  '<b>Matching Articles</b><br/>'
    for matchingArticleId in matchingArticleIds:
        matchingArticle = articleIdToArticleMapping[matchingArticleId]['headline_text']
    
        displayString +=  '<b>'+matchingArticleId+'</b>:  '+matchingArticle + '<br/>'
        
    
    return displayString
    

app.run()