import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

X = X/np.amax(X,axis=0) 
y = y/100

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)

epoch=7000 
lr=0.1 		
n_input = 2
n_hidden = 3
n_output = 1 	

wh=np.random.uniform(size=(n_input,n_hidden))  
bh=np.random.uniform(size=(1,n_hidden))
wout=np.random.uniform(size=(n_hidden,n_output))
bout=np.random.uniform(size=(1,n_output))

for i in range(epoch):
    hlayer = sigmoid(np.dot(X, wh) + bh)
    output = sigmoid(np.dot(hlayer, wout) + bout)

    d_output = (y-output)* derivatives_sigmoid(output)
    d_hiddenlayer = d_output.dot(wout.T) * derivatives_sigmoid(hlayer)

    wout += hlayer.T.dot(d_output) *lr
    wh += X.T.dot(d_hiddenlayer) *lr

print("Input: \n" + str(X)) 
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" ,output)
