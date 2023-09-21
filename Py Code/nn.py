import numpy as np
from numpy import ma
import pandas as pd

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)


def create_neural_net(input_size,ip_layer_size,h_layer_size,op_layer_size,epoch,alpha):

    X = np.random.randint(2,size=(ip_layer_size,input_size))
    print("\n\nInput Data Set:\n")
    print(X);
    
    
    y = np.random.randint(2,size=(op_layer_size,input_size))
    print("\n")
    print(y[1]);
    
    
    num_iterations=epoch
    lr=alpha
    inputlayer_neurons = X.shape[0]
    m= X.shape[1]
    print("m=",m)
    hiddenlayer_neurons = h_layer_size
    output_neurons = op_layer_size
    
    wh=np.random.randn(hiddenlayer_neurons,inputlayer_neurons)
    bh=np.random.randn(hiddenlayer_neurons,1)
    wout=np.random.randn(output_neurons,hiddenlayer_neurons)
    bout=np.random.randn(output_neurons,1)
    
    print("\n\nnum of iteration= ",num_iterations)
    print("learning rate= ",lr)
    print("num of input neurons= ",inputlayer_neurons)
    print("num of hidden neurons= ",hiddenlayer_neurons)
    print("num of output neurons= ",output_neurons)
    print("\nwhs\n= ",wh)
    print("\nbhs\n= ",bh[1:5])
    print("\nwout\n= ",wout)
    print("\nbout\n= ",bout)
    
    
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


weights= create_neural_net(200,1000,300,5,500,0.099)

X = np.random.randint(2,size=(1000,100))
     
y = np.random.randint(2,size=(5,100))
    
op=predict(X,weights[0],weights[1],weights[2],weights[3])
    
res=np.abs(y-op)

acc=(500-np.count_nonzero(res))/5
print("Accuracy= ",acc,"%")




