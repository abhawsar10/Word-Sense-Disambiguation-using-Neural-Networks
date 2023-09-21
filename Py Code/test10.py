from nltk.corpus import brown
import gensim
from nltk.corpus import wordnet as wn
from nltk.corpus import senseval
import numpy as np
import pickle

from gensim.models import Word2Vec 
model = Word2Vec.load("word2vec.model")

alic=model1.wv.most_similar('interest',topn=5000)

for i in range(10):
   print(i,alic[i][0],alic[i][1])
    
definitions=['readiness to give attention','quality of causing attention to be given to','activity, etc. that one gives attention to','advantage, advancement or favor','a share in a company or business','money paid for the use of money']

num_sent=2368
num_senses=6

featurevec=np.zeros(shape=(num_sent,1000),dtype='int')
opvec=np.zeros(shape=(num_sent,num_senses),dtype='int')
k=0
for inst in senseval.instances('interest.pos')[0:num_sent]:
    p = inst.position
    
    left = ' '.join(w for (w,t) in inst.context[0:p])
    word = ' '.join(w for (w,t) in inst.context[p:p+1])
    right = ' '.join(w for (w,t) in inst.context[p+1:])
    senses = ' '.join(inst.senses)
    #print('%20s |%10s | %-15s -> %s' % (left, word, right, senses))

    lchar=senses[len(senses)-1:len(senses)]
    sens=int(lchar,10)-1
    
    sent1=left+" "+word+" "+right
    sent=sent1.split()
    #print(sent)
    l=len(sent)
    #print(l)
    #print("Sense=",sens)
    
    opvec[k][sens]=1
    
    for i in range(1000):
        for j in range(l):
            if alic[i][0]==sent[j]:
                featurevec[k][i-1]=1
    #print(k)
    k=k+1

#print(featurevec)
    
Xtrain=featurevec.transpose()
Ytrain=opvec.transpose()

print("size of X=",np.shape(Xtrain))

Xtest=Xtrain[:,1651:]
Xtrain=Xtrain[:,:1650]

Ytest=Ytrain[:,1651:]
Ytrain=Ytrain[:,:1650]

print("size of Xtrain=",np.shape(Xtrain))
print("size of XTest=",np.shape(Xtest))
print("size of YTrain=",np.shape(Ytrain))
print("size of YTest=",np.shape(Ytest))


print("Number of non zeros=",np.count_nonzero(Xtrain))  
print("Number of non zeros=",np.count_nonzero(Ytrain,axis=1))  
print("Number of non zeros=",np.count_nonzero(Xtest))  
print("Number of non zeros=",np.count_nonzero(Ytest,axis=1))  

with open("Xtr.txt", "wb") as fp:   #Pickling
    pickle.dump(Xtrain, fp)

with open("Xte.txt", "wb") as fp:   #Pickling
    pickle.dump(Xtest, fp)
    
with open("Ytr.txt", "wb") as fp:   #Pickling
    pickle.dump(Ytrain, fp)

with open("Yte.txt", "wb") as fp:   #Pickling
    pickle.dump(Ytest, fp)

