from preprocessing import *
import os.path
from os import path
import sys
import pickle
import numpy as np
from nltk.corpus import brown
import gensim
from gensim.models import Word2Vec 
from nncomponents import *
from nltk.corpus import wordnet as wn

def findambiwords(wordlist):
      
    awords=[]    
    for w in wordlist:
        if path.exists("Z:\\BE Project\\Data Storage\\Final NN Models\\"+w+"_params.txt"):
            awords.append(w)        
    #print(awords)    
    if not awords:
        print("No words in sentence are classified as ambiguous...")
        return None
    else:
        return awords
        
def loadparams(awords):
    
    paramlist=[]
    for i in range(len(awords)):  
        params={}      
        with open("Z:\\BE Project\\Data Storage\\Final NN Models\\"+awords[i]+"_params.txt", "rb") as fp:   #Pickling     
            params=pickle.load(fp)
        paramlist.append(params)
    return paramlist;

def createfeaturevec(awords,wordlist,fvec_size):
    
    veclist=[]
    model1 = Word2Vec.load("word2vec.model")
    l=len(wordlist)
        
    for k in range(len(awords)):
        fvec=np.zeros(shape=(fvec_size[k],1),dtype='int')
        alic=model1.wv.most_similar(awords[k],topn=5000)
        
        for i in range(fvec_size[k]):
            for j in range(l):
                if alic[i][0]==wordlist[j]:
                    fvec[i][0]=1
                    #print("x==",i)
                    
        veclist.append(fvec)
        
    #print(fvec)
    #print(np.size(fvec,axis=0),np.size(fvec,axis=1))
    #print(print("Number of non zeros=",np.count_nonzero(fvec)))
    return veclist


def predict(X, parameters):
    
    m = X.shape[1]
    n = len(parameters) // 2 
    p = np.zeros(((parameters["b"+str(n)].shape[0]),m),dtype='int')
    #p = np.zeros((y.shape[0],m))
    
    probas, caches = L_model_forward(X, parameters)

    maxv=np.zeros(shape=(len(probas[0]),),dtype='float')
    xval=np.zeros(shape=(len(probas[0]),),dtype='int')
    yval=np.zeros(shape=(len(probas[0]),),dtype='int')
    
    for i in range(len(probas[0])):
        maxv[i]=probas[0][i]
        xval[i]=0
        yval[i]=i
        for j in range(len(probas)):
            if probas[j][i]>maxv[i]:
                #print(probas[j][i])
                maxv[i]=probas[j][i]
                #print(maxv[i])
                xval[i]=j
                yval[i]=i
    
    #print("y=",y)
    #print("probas",probas)
    
    #print("maxv=",maxv)
    #print("xval",xval)
    #print("yval",yval) 
    
    for i in range(len(probas[0])):      
        p[xval[i]][yval[i]]=1
        
    return xval[0]
    
def retdefinition(aword,senseno):
    
    syn=wn.synsets(aword)
    return str(syn[senseno].definition())

def findops(awords,userip_vecs,params):
    
    #print(len(awords))
    #print(len(userip_vecs))
    #print(len(params))
    result={}
    for i in range(len(awords)):
        sense_no=predict(userip_vecs[i],params[i])
        #print("\nAmbiguous word= ",awords[i]) 
        #print("Predicted Sense Number= ",sense_no)
        #print("Definition of Sense= ",retdefinition(awords[i],sense_no))
        result["Aword"+str(i)]=awords[i]
        result["Sense"+str(i)]=sense_no
        result["Def"+str(i)]=retdefinition(awords[i],sense_no)
    return result
        
        





#str1=input("Enter String\n")
#str1="piano bass hello hello play guitar banjo"
#str1="This is a amortized crown sample play piano bass guitar, play apply showing off the stop words filtration."  
#str1="Eating in bed is easier said than done, as it is heavily dependant on the bedding clothing"
#str1="the dentist put a crown on my tooth"

#wordlist=preprocess(str1)                               #get list of words in sentence
#awords=findambiwords(wordlist)                          #find ambiguous words

def run_user_end(wordlist,awords):
    
    fvec_size=np.zeros(shape=(len(awords),),dtype='int')    
    params=loadparams(awords)                               #load neural network
    for i in range(len(params)):                            
        fvec_size[i]=len(params[i]["W1"][0])                #find size of features
    userip_vecs=createfeaturevec(awords,wordlist,fvec_size) #find input features
        
    return findops(awords,userip_vecs,params)                      #predict and display
    
        

#print(run_user_end(wordlist,awords))


