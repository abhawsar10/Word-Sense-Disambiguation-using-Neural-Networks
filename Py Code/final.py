import numpy as np
from numpy import ma
import pandas as pd
import pickle


def sigmoid (x):
    return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)


def create_neural_net(X,y,input_size,ip_layer_size,h_layer_size,op_layer_size,epoch,alpha):

     
    num_iterations=epoch
    lr=alpha
    inputlayer_neurons = X.shape[0]
    m= X.shape[1]
    print("m=",m)
    hiddenlayer_neurons = h_layer_size
    output_neurons = op_layer_size
    
    wh=np.random.rand(hiddenlayer_neurons,inputlayer_neurons)
    bh=np.zeros((hiddenlayer_neurons,1))
    wout=np.random.rand(output_neurons,hiddenlayer_neurons)
    bout=np.zeros((output_neurons,1))
    
    print("\n\nnum of iteration= ",num_iterations)
    print("learning rate= ",lr)
    print("num of input neurons= ",inputlayer_neurons)
    print("num of hidden neurons= ",hiddenlayer_neurons)
    print("num of output neurons= ",output_neurons)
    print("\nwhs size\n= ",np.shape(wh))
    print("\nbhs size\n= ",np.shape(bh))
    print("\nwout size\n= ",np.shape(wout))
    print("\nbout size\n= ",np.shape(bout))
    
    
    print("\nCosts:\n---------------------------------------------------------")
    
    for i in range(num_iterations):
        #forward prop
        hidden_layer_input1=np.dot(wh,X)
        hidden_layer_input=hidden_layer_input1 + bh
        hiddenlayer_activations = sigmoid(hidden_layer_input)
        output_layer_input1=np.dot(wout,hiddenlayer_activations)
        output_layer_input= output_layer_input1+ bout
        output = sigmoid(output_layer_input)
        
        #m= X.shape[1]
        #print("m=",m)
        
        cost=np.sum(np.sum(-(np.multiply(y,ma.log(output)) + np.multiply(np.subtract(1,y),ma.log(np.subtract(1,output))))))/m   
        if i%100==0:
            print("Cost after ",i,"iterations: ",cost)
         
        #print("output",output.shape[0],"x",output.shape[1])
        #print("y",y.shape[0],"x",y.shape[1])
        
        #back prop
        E=-(np.multiply(y,ma.log(output)) + np.multiply(np.subtract(1,y),ma.log(np.subtract(1,output))))                
        
        #print("E",E.shape[0],"x",E.shape[1])
        
        slope_output_layer = derivatives_sigmoid(output)
        slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
        d_output = np.multiply(E,slope_output_layer)
        Error_at_hidden_layer = np.dot(wout.T,d_output)
        d_hiddenlayer = np.multiply(Error_at_hidden_layer,slope_hidden_layer)
        
        wout += np.dot(d_output,hiddenlayer_activations.T) *lr
        bout += np.sum(d_output, axis=1,keepdims=True) *lr
        wh += np.dot(d_hiddenlayer,X.T) *lr
        bh += np.sum(d_hiddenlayer, axis=1,keepdims=True) *lr
    
    print("Final Cost: ",cost)
    return [wh,bh,wout,bout]
    
def predict(X,wh,bh,wout,bout):
    
    hidden_layer_input1=np.dot(wh,X)
    hidden_layer_input=hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input1=np.dot(wout,hiddenlayer_activations)
    output_layer_input= output_layer_input1+ bout
    output = sigmoid(output_layer_input)
    
    return output




with open("Xtr.txt", "rb") as fp:   # Unpickling
    Xtrain = pickle.load(fp)
with open("Xte.txt", "rb") as fp:   # Unpickling
    Xtest = pickle.load(fp)
with open("Ytr.txt", "rb") as fp:   # Unpickling
    Ytrain = pickle.load(fp)
with open("Yte.txt", "rb") as fp:   # Unpickling
    Ytest = pickle.load(fp)
    
print("Number of non zeros=",np.count_nonzero(Xtrain))  
print("Number of non zeros=",np.count_nonzero(Ytrain,axis=1))  
print("Number of non zeros=",np.count_nonzero(Xtest))  
print("Number of non zeros=",np.count_nonzero(Ytest,axis=1)) 

ip_size=Xtrain.shape[1]
print("\nIP number of datasets=",ip_size)
ip_layer_size=Xtrain.shape[0]
print("\nNumber of nodes in IP layer=",ip_layer_size)
hidden_layer_nodes=100
print("\nNumber of nodes in hidden layer=",hidden_layer_nodes)
op_layer_nodes=Ytrain.shape[0]
print("\nNumber of nodes in output layer=",op_layer_nodes)
epoch=500
print("\nEpoch=",epoch)
alpha=0.099
print("\nAlpha=",alpha)
print("--------------------------------------------------")

weights= create_neural_net(Xtrain,Ytrain,ip_size,ip_layer_size,hidden_layer_nodes,op_layer_nodes,epoch,alpha)

op=predict(Xtest,weights[0],weights[1],weights[2],weights[3])
    
res=np.abs(Ytest-op)

print(Ytest)
print(Ytest.shape)

print(op)
print(op.shape)

print(res)
print(res.shape)

sum=np.count_nonzero(res,axis=0)
print(sum)
print(sum.shape)

test_ip_size=Ytest.shape[1]

acc=((test_ip_size-np.count_nonzero(sum))*100)/test_ip_size

print("no of non zeros",np.count_nonzero(sum))
print("Accuracy= ",acc,"%")





















