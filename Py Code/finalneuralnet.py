import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from dnn_app_utils_v3 import *
import pickle

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







with open("Xtr.txt", "rb") as fp:   
    Xtrain = pickle.load(fp)
with open("Xte.txt", "rb") as fp:   
    Xtest = pickle.load(fp)
with open("Ytr.txt", "rb") as fp:   
    Ytrain = pickle.load(fp)
with open("Yte.txt", "rb") as fp:   
    Ytest = pickle.load(fp)
    
    
print ("Xtrain's shape: " + str(Xtrain.shape))
print ("Ytrain's shape: " + str(Ytrain.shape))
print ("Xtest's shape: " + str(Xtest.shape))
print ("Ytest's shape: " + str(Ytest.shape))
print("Number of non zeros=",np.count_nonzero(Xtrain))  
print("Number of non zeros=",np.count_nonzero(Ytrain,axis=1))  
print("Number of non zeros=",np.count_nonzero(Xtest))  
print("Number of non zeros=",np.count_nonzero(Ytest,axis=1)) 

print("--------------------------------------------------")


### INPUTS TO NEURAL NET ####
epoch=1200
alpha=0.0022
printeveryn=100


layers_dims = [1000, 75, 10, 6]


print("Number of nodes in input layer=",layers_dims[0])
print("Number of nodes in hidden layer=",layers_dims[1])
print("Number of nodes in hidden layer=",layers_dims[2])
print("Number of nodes in output layer=",layers_dims[3])

print("\nEpoch=",epoch)
print("\nAlpha=",alpha)
print("--------------------------------------------------")




parameters = L_layer_model(Xtrain, Ytrain, layers_dims,learning_rate = alpha, num_iterations = epoch, print_cost = True)



pred_train = predict(Xtrain, Ytrain, parameters)

pred_train = predict(Xtest, Ytest, parameters)


















