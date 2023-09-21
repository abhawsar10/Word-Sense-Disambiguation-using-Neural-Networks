import gensim


from nltk.corpus import webtext
from nltk.corpus import brown
from nltk.corpus import reuters
    

def createembeddingmodel(corpus):
    
    if corpus == "reuters":
        data=reuters.sents()
    if corpus == "webtext":
        data=webtext.sents()
    if corpus == "brown":
        data=brown.sents()
        
    #print(data)
    
    model1 = gensim.models.Word2Vec(data, min_count = 1,  
                                  size = 100, window = 5,hs=1, negative=0) 
      
    # Print results 
    print("Embedding model 'word2vec.model 'created")
    model1.save("word2vec.model")


createembeddingmodel("reuters")