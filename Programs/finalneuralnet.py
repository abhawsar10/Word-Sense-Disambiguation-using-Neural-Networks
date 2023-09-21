import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from nncomponents import *
import pickle
from nltk.corpus import wordnet as wn

#%matplotlib inline
plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

#%load_ext autoreload
#%autoreload 2

np.random.seed(1)




def L_layer_model(X, Y, layers_dims, learning_rate = 0.0075, num_iterations = 3000, print_cost=False):#lr was 0.009
    
    np.random.seed(1)
    costs = []                         
    
    parameters = initialize_parameters_deep(layers_dims)
  
    for i in range(0, num_iterations):

        AL, caches = L_model_forward(X,parameters)
        
        cost = compute_cost(AL,Y)
    
        grads = L_model_backward(AL,Y,caches)
        
        parameters = update_parameters(parameters,grads,learning_rate)
        
                
        if print_cost and i % 100 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
        if print_cost and i % 100 == 0:
            costs.append(cost)
            
    # plot the cost function
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundreds)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    
    return parameters


def run_neural_net(aword,epoch=1200,alpha=0.0022,printeveryn=100):
    
    
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xtr.txt", "rb") as fp:   #Pickling     
        Xtrain = pickle.load(fp)
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xte.txt", "rb") as fp:   #Pickling       
        Xtest = pickle.load(fp)
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Ytr.txt", "rb") as fp:   #Pickling      
        Ytrain = pickle.load(fp)
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Yte.txt", "rb") as fp:   #Pickling     
        Ytest = pickle.load(fp)
        
        
    print ("Xtrain's shape: " + str(Xtrain.shape))
    print ("Ytrain's shape: " + str(Ytrain.shape))
    print ("Xtest's shape: " + str(Xtest.shape))
    print ("Ytest's shape: " + str(Ytest.shape))
    #print("Number of non zeros=",np.count_nonzero(Xtrain))  
    #print("Number of non zeros=",np.count_nonzero(Ytrain,axis=1))  
    #print("Number of non zeros=",np.count_nonzero(Xtest))  
    #print("Number of non zeros=",np.count_nonzero(Ytest,axis=1)) 
    print("Data loaded from file...")
    print("--------------------------------------------------")
    
    
    num_senses=len(wn.synsets(aword))
    inputlaynodes=Xtrain.shape[0]
    
    layers_dims = [inputlaynodes, 275, 110, num_senses]
    
    
    
    print("Number of nodes in input layer=",layers_dims[0])
    print("Number of nodes in hidden layer=",layers_dims[1])
    print("Number of nodes in hidden layer=",layers_dims[2])
    print("Number of nodes in output layer=",layers_dims[3])
    
    print("\nEpoch=",epoch)
    print("\nAlpha=",alpha)
    print("--------------------------------------------------")
    
    
    
    
    parameters = L_layer_model(Xtrain, Ytrain, layers_dims,learning_rate = alpha, num_iterations = epoch, print_cost = True)
    
    #with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xtr.txt", "rb") as fp:   #Pickling     
     #   Xtrain = pickle.load(fp)
    
    L = len(parameters)//2  
        
    #for l in range(L):
        #print("W",l,"=")
        #print(parameters["W" + str(l+1)])
        #print("b",l,"=")
        #print(parameters["b" + str(l+1)])
           
    
    pred_train = predict(Xtrain, Ytrain, parameters)
    
    pred_train = predict(Xtest, Ytest, parameters)
    
    with open("Z:\\BE Project\\Data Storage\\Final NN Models\\"+aword+"_params.txt", "wb") as fp:   #Pickling     
        pickle.dump(parameters,fp)



aword=input("Enter Amiguous Word:  ")
run_neural_net(aword)












