import sys
args = sys.argv
inp = args[1]
out = args[2]

f = open(inp,"r")
lis = f.read()
LIS = lis.split("\n")
LIS = LIS[:-1]
X = []
Y = []
C = []

import numpy as np
import matplotlib as plt
LIST = []
for i in LIS[1:]:
    I = i.split(',')
    LIST.append(I)    
    x = float(I[0])
    y = float(I[1])
    
    if I[2] == '1':
        c = 'red'
    elif I[2] == '0':
        c = 'blue'
    X.append(x)
    Y.append(y)
    C.append(c)

AM = []
for l in LIST:
    L = []
    for i in l:
        L.append(float(i))
    AM.append(L)    

def perceptron(X):
    """
    The perceptron Algorithm
    """
    def update(w,x):
        X= []
        y=dic[x]
        for i in x:            
            X.append(i*y) 
        W= []
        for j in range(len(w)):
            W.append(w[j] + X[j])
        Out = open(out, "a+")
        Out.write("%s,%s,%s\n" % (W[0], W[1], W[2]))    
        return W    
                    
            
    def sign(x,w):
        S = 0
        for j in range(len(x)):
            S += (x[j]*w[j])
        if S > 0 :
            return 1
        elif S < 0:
            return -1
        elif S == 0:
            return 0
        
    dic = {}
    
    for x in X:
        dic[(x[0],x[1],1)] = x[2]
#    return dic
    w1 = 0
    w2 = 0
    b = 0
    w  = [w1,w2,b]
    while True:
        mis = []
        for x in dic.keys():
            if dic[x] != sign(x,w):
                mis.append(x)
        if len(mis) == 0:
            Out = open(out, "a+")
            Out.write("%s,%s,%s\n" % (w[0], w[1], w[2])) 
            return w
        else:
            a = np.random.randint(0,len(mis))
            w=update(w,mis[a])
                
        
abc = perceptron(AM) 
#plt.pylab.scatter(X,Y, color = C)    
#m=-3
#w2 = abc[1]
#w1 = abc[0]
#b=abc[2]
#plt.pylab.plot([0,20],[b/-w2, (20*w1/-w2 )+ (b/-w2) ], c = 'g')
