# Self Organizing Maps

# Unsupervised Deep Learning identify patterns high dimension dataset
# one of these patterns will find the fradulant way
# segmentcorrespond to specific range of values SOM
# customers are input to new space, each neuron initialised,

# winning node, guassian neighbouring function closer to the point, input space
# output space reduces dimensions, obtain with all the winning nodes
# frauds are outliers, how to detect, mean euclidean distance between in neighborhood,
# far in neurons in self-organizing maps, inverse function input associated with winning node

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# dataset => https://archive.ics.uci.edu/ml/datasets/statlog+(australian+credit+approval)
# split the dataset from Customer ID to attribute to 14 and (yes or no been approve)
# clearly distinguish who got approved and not, in priority of fradulant customers who got approved
dataset = pd.read_csv('Credit_Card_Applications.csv')

# iloc gets indexes of observation, all the lines we use : and all the columns except 
# last so :-1 and values
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# split dataset into X & Y, not trying to do supervised learning or 0 or 1 classification
# making distinction of approved and not approved customers, train SOM we will only use
# X and there's no dependent variable 

# Feature Scaling - compulsory for deep learning becase we're starting with a high 
# dimensional dataset with lots of non-linear relationship and it will be much easier
# for our deep learning models to be trained if the features are scaled. 
# use normalization all features from 0 to 1
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))

# fit sc object to X so sc gets all info (min and max) and all info for normalization
# apply normalization to X, fit method returns normalized version of X
X = sc.fit_transform(X)
