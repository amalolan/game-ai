# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:29:34 2017

@author: Malolan
"""

import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn import linear_model
from sklearn import neighbors
from sklearn import tree
from sklearn import ensemble
from sklearn import preprocessing
from sklearn import metrics
import time
start = time.time()
args = sys.argv
inp = args[1]
out = args[2]
Out = open(out,'w')
Out.close()

data = pd.read_csv(inp, header=None)
X = data.iloc[1:,0:2]
y = data.iloc[1:,2]



xtrain,xtest,ytrain,ytest = train_test_split(X,y,test_size = 0.4,stratify = y)


#SVM with Linear Kernel
tuned_parameters = [{'kernel': ['linear'], 'C': [0.1, 0.5, 1, 5, 10, 50, 100]}]
clf = GridSearchCV(svm.SVC(kernel='linear'),tuned_parameters,cv=5,scoring='accuracy')    
clf.fit(xtrain,ytrain)
best = clf.best_score_
prediction = clf.score(xtest,ytest)
prediction = metrics.accuracy_score(ytest,clf.predict(xtest))
Out = open(out, "a+")
Out.write("%s,%s,%s\n" % ('svm_linear',best,prediction))
Out.close()
print('SVM with Linear Kernel')
#SVM with poly kernel
#tuned_parameters = [{'kernel': ['poly'],'C':[0.1, 1, 3],'degree':[4,5,6],'gamma':[0.1, 1]}]
#clf = GridSearchCV(svm.SVC(kernel='poly'),tuned_parameters,cv=5,scoring='accuracy')
#clf.fit(xtrain,ytrain)
#best = clf.best_score_
#prediction = clf.score(xtest,ytest)
Out = open(out, "a+")
Out.write("%s,%s,%s\n" % ('svm_polynomial',0,0))
Out.close()
print('SVM with Polynomial Kernel')
#SVM with rbf kernel
tuned_parameters = [{'kernel': ['rbf'],'C':[0.1, 0.5, 1, 5, 10, 50, 100],'gamma': [0.1, 0.5, 1, 3, 6, 10]}]
clf = GridSearchCV(svm.SVC(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(xtrain,ytrain)
best = clf.best_score_
prediction = clf.score(xtest,ytest)
prediction = metrics.accuracy_score(ytest,clf.predict(xtest))
Out = open(out, "a+")
Out.write("%s,%s,%s\n" % ('svm_rbf',best,prediction))
Out.close()
print('SVM with rbf kernel')
#Logistic regression
clf = GridSearchCV(linear_model.LogisticRegression(),[{'C' : [0.1, 0.5, 1, 5, 10, 50, 100]}],
                   cv=5,scoring='accuracy')
clf.fit(xtrain,ytrain)
best = clf.best_score_
prediction = clf.score(xtest,ytest)
prediction = metrics.accuracy_score(ytest,clf.predict(xtest))
Out = open(out, "a+")
Out.write("%s,%s,%s\n" % ('logistic',best,prediction))
Out.close()
print('Logistic regression')
#KNN
nn = []
nm=[]
for i in range(1,51):
    nn.append(i)
for i in range(5,61,5):
    nm.append(i)       
    
tuned_parameters=[{'n_neighbors':nn,'leaf_size':nm}]
clf = GridSearchCV(neighbors.KNeighborsClassifier(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(xtrain,ytrain)
best = clf.best_score_
prediction = clf.score(xtest,ytest)
prediction = metrics.accuracy_score(ytest,clf.predict(xtest))
Out = open(out, "a+")
Out.write("%s,%s,%s\n" % ('knn',best,prediction))
Out.close()
print('KNN')
#Decision Tree
tuned_parameters= [{'max_depth':nn ,'min_samples_split':[2,3,4,5,6,7,8,9,10]}]
clf = GridSearchCV(tree.DecisionTreeClassifier(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(xtrain,ytrain)
best = clf.best_score_
prediction = clf.score(xtest,ytest)
prediction = metrics.accuracy_score(ytest,clf.predict(xtest))
Out = open(out, "a+")
Out.write("%s,%s,%s\n" % ('decision_tree',best,prediction))
Out.close()
print('Decision Tree')
#Random Forest
tuned_parameters= [{'max_depth':nn ,'min_samples_split':[2,3,4,5,6,7,8,9,10]}]
clf = GridSearchCV(ensemble.RandomForestClassifier(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(xtrain,ytrain)
best = clf.best_score_
prediction = clf.score(xtest,ytest)
prediction = metrics.accuracy_score(ytest,clf.predict(xtest))
Out = open(out, "a+")
Out.write("%s,%s,%s\n" % ('random_forest',best,prediction))
Out.close()
print('Random Forest')
end = time.time()
print(start-end)
