import pandas as pd
from config import *
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import sys,os
import numpy as np

# Load the csv file
df = pd.read_csv(datapath)

#add features
if len(ADD_FEATURES) != 0:
    for feat in ADD_FEATURES :
        df[feat] = np.log(df['Petal_Length'])

    rawfields += ADD_FEATURES

# Select independent and dependent variable
X = df[rawfields]
y = df[target]


# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize, random_state=randomstate)

 #Call Feature engineering function from feature.py

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Make pickle file of our model
pickle.dump(classifier, open(modeloutput, "wb"))

#Load the saved model
model = pickle.load(open(modeloutput, "rb"))

#Predictions
output = model.predict(X_test)