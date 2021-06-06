# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:08:11 2017

@author: Malolan
Linear Regression w/ gradient descent
"""
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
Z = []
Out = open(out,'w')
Out.close()
import numpy as np
import matplotlib as plt
LIST = []
for i in LIS:
    I = i.split(',')
    LIST.append(I)    
    x = float(I[0])
    y = float(I[1])
    z= float(I[2])
    X.append(x)
    Y.append(y)
    Z.append(z)


AM = []
for l in LIST:
    L = []
    for i in l:
        L.append(float(i))
    AM.append(L)    
def plotty(X,Y,Z):
    fig = plt.pylab.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X,Y,Z)
    plt.pylab.show()
def normalization(AM):    
    """
    Normalizes age and weight
    """
    age = []
    
    weight = []
    height = []    
    for i in AM:
        age.append(i[0])
        weight.append(i[1])
        height.append(i[2])
    am = np.mean(age)
    astd = np.std(age)
    wm = np.mean(weight)
    wstd = np.std(weight)
    Nage = []
    Nweight = []
    Nheight = height[:]
    for i in age:
        ni = (i-am)/astd
        Nage.append(ni)
    for i in weight:
        ni = (i-wm)/wstd
        Nweight.append(ni)
    NAM = []
    for j in range(len(age)):
        NAM.append([Nage[j],Nweight[j],Nheight[j]])
    return NAM

def decent(NAM):
    def update(betas,alpha):
        BETAS = [0,0,0]
        BE = betas[:]
        def f(i) :
            return BE[0] + BE[1]*age[i] + BE[2]*height[i]
        for b in range(len(BE)):    
            SUM = 0
            for i in range(len(age)):
                
                if b == 0:
                    j=  1
                elif b == 1:
                    j = age[i]
                elif b == 2:
                    j = weight[i]
                SUM+= (f(i) - height[i])*j   
            BETAS[b] = (BE[b]- (alpha*SUM*(1/len(age))))
        return BETAS    
    
    age = []
    weight = []
    height = []    
    for i in NAM:
        age.append(i[0])
        weight.append(i[1])
        height.append(i[2])


    AL =  [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 3]
    n=100
    for alpha in AL:
        betas = [0,0,0]
        for RANGE in range(n):
            betas = update(betas,alpha)

        Out = open(out, "a+")
        Out.write("%s,%s,%s,%s,%s\n" % (alpha,n,betas[0], betas[1], betas[2]))     
       
            
#decent(normalization(AM))        

        
