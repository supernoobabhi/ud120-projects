#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
# Using gaussian naive bayes
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
# print(clf.predict([[-0.8, -1]]))
t0 = time()
pre=clf.predict(features_test);
print "predicting time:", round(time()-t0, 3), "s"
# Checking accuracy
from sklearn.metrics import accuracy_score
# y_pred = [0, 2, 1, 3];
# y_true = [0, 1, 2, 3];
print(accuracy_score(labels_test, pre))

#########################################################


