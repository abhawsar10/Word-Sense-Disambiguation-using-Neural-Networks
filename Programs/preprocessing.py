from nltk.stem import PorterStemmer
import nltk
ps = PorterStemmer() 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
from nltk.corpus import wordnet


def preprocess(example_sent):
    
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(example_sent) 
    filt = []   
    
    for w in word_tokens: 
        if w not in stop_words and w.isalpha(): 
            filt.append(w) 
      
    #print("after tokenization:\n",word_tokens) 
    #print("after filtration:\n",filt) 
    filt=[f.lower() for f in filt]
    filt=[lemmatizer.lemmatize(f,pos='n') for f in filt]
    filt=[lemmatizer.lemmatize(f,pos='v') for f in filt]
    filt=[lemmatizer.lemmatize(f,pos='a') for f in filt]
    
    for i in range(len(filt)):
        if filt[i].endswith("ily"): 
            filt[i]=filt[i][:-3]+"y"
    return filt
    














