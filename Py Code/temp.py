import numpy as np
import pandas as pd

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)

df = np.random.randint(2,size=(5,4))

print("df",df)

X=np.array([[1,1,0,0],[0,1,1,0],[1,0,1,0]])

print("\n\nInput Data Set:\n")
print(X);

y=np.array([[1],[0],[1]])
print("\n")
print(y);


num_iterations=5001
lr=0.1
inputlayer_neurons = X.shape[1]
m= X.shape[0]
hiddenlayer_neurons = 3
output_neurons = 1

wh=np.random.randn(inputlayer_neurons,hiddenlayer_neurons)
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))

print("\n\nnum of iteration= ",num_iterations)
print("learning rate= ",lr)
print("num of input neurons= ",inputlayer_neurons)
print("num of hidden neurons= ",hiddenlayer_neurons)
print("num of output neurons= ",output_neurons)
print("\nwhs\n= ",wh)
print("\nbhs\n= ",bh)
print("\nwout\n= ",wout)
print("\nbout\n= ",bout)


print("\nCosts:\n---------------------------------------------------------")

for i in range(num_iterations):
    #forward prop
    hidden_layer_input1=np.dot(X,wh)
    hidden_layer_input=hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input1=np.dot(hiddenlayer_activations,wout)
    output_layer_input= output_layer_input1+ bout
    output = sigmoid(output_layer_input)
    
    cost=(np.sum((y-output)**2))/m
    if i%500==0:
        print("Cost after ",i,"iterations: ",cost)
        
    
    #back prop
    E = y-output
    slope_output_layer = derivatives_sigmoid(output)
    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    
    print("size of slope_hd_ly",hiddenlayer_activations.shape[0],"x",hiddenlayer_activations.shape[1])
    
    wout += hiddenlayer_activations.T.dot(d_output) *lr
    bout += np.sum(d_output, axis=0,keepdims=True) *lr
    wh += X.T.dot(d_hiddenlayer) *lr
    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr

print("\nOutput\n",output)

