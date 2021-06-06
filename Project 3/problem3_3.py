# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:58:50 2017

@author: Malolan
"""
import numpy as np
import matplotlib as plt
import sys
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
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


LIST = []
for i in LIS:
    I = i.split(',')
    LIST.append(I)    
    x = I[0]
    y = I[1]
    
    if I[2] == '1':
        c = 'red'
    elif I[2] == '0':
        c = 'blue'    
    else:
        c = None
    if x != 'A':     
        X.append(x)
        Y.append(y)
        C.append(c)
AM = []
for l in LIST[1:]:
    L = []
    for i in l[:-1]:
        L.append(float(i))
    L.append(int(l[-1]))    
    AM.append(L)  
plt.pylab.scatter(X,Y,color = C)     
X = np.array(X)
Y = np.array(Y)
C = np.array(C)
