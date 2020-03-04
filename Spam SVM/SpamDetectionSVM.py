# -*- coding: utf-8 -*-
"""SpamDetectionPerceptron

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bs9kSUI43P1lGiyAExi5D4qssA7c6eCC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

#read dataset "phishing_dataset" into dataframe "df"
df = pd.read_csv("phishing_dataset.csv")

# Seperate the dataframe into two values
# y, last column in the dataset
# x, rest of the dataset 
y = df.iloc[:, -1].values
x = df.iloc[:, 0:-1].values


# Use "train_test_split" to randomly generate dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)


# Use Perceptron function and fit x_train and y_train to it 
# max_iter : number of passes ofver the training data (aka 'epochs')
# eta0 : Constant by which updates are multiplied 
p = Perceptron(max_iter=40, eta0=.3, random_state=0)
p.fit(x_train, y_train)

y_pred = p.predict(x_test)

# Determine difference between number of samples and predicted samples 
# Measure accuracy of the Perceptron 
print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))