from nltk.corpus import brown
import gensim
from nltk.corpus import wordnet as wn
from nltk.corpus import senseval
import numpy as np
import pickle
import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from dnn_app_utils_v3 import *
import pickle

k=500

with open("Xtr.txt", "rb") as fp:   
    Xtrain = pickle.load(fp)
with open("Xte.txt", "rb") as fp:   
    Xtest = pickle.load(fp)
with open("Ytr.txt", "rb") as fp:   
    Ytrain = pickle.load(fp)
with open("Yte.txt", "rb") as fp:   
    Ytest = pickle.load(fp)


print("size of Xtrain=",np.shape(Xtrain))
print("size of XTest=",np.shape(Xtest))
print("size of YTrain=",np.shape(Ytrain))
print("size of YTest=",np.shape(Ytest))


X=np.concatenate((Xtrain,Xtest),axis=1)

print ("X's shape: " + str(X.shape))

Xmean=X.mean(1).reshape(X.shape[0],1)

#print(Xmean)
#print(Ymean)

print ("Xmean's shape: " + str(Xmean.shape))

X=(X-Xmean)

print ("X's shape: " + str(X.shape))


sigma=X.dot(X.T)/X.shape[1]

print ("Sigma's shape: " + str(sigma.shape))

U = []
S = []

U,S,Vh=np.linalg.svd(sigma)

print ("U's shape: " + str(U.shape))

Ureduce=U[:,0:k]

Z=Ureduce.T.dot(X)


print ("Z's shape: " + str(Z.shape))


Xtrain=Z[:,:1650]
Xtest=Z[:,1651:]

print ("Xtrain's shape: " + str(Xtrain.shape))
print ("Xtest's shape: " + str(Xtest.shape))

with open("Xtr.txt", "wb") as fp:   #Pickling
    pickle.dump(Xtrain, fp)

with open("Xte.txt", "wb") as fp:   #Pickling
    pickle.dump(Xtest, fp)
    
with open("Ytr.txt", "wb") as fp:   #Pickling
    pickle.dump(Ytrain, fp)

with open("Yte.txt", "wb") as fp:   #Pickling
    pickle.dump(Ytest, fp)














