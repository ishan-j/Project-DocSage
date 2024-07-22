# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:59:06 2024

@author: Pratesh Mishra
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import os
df = pd.read_csv("non-encoded.csv")

le= LabelEncoder()
def label_encode_dataframe(df):
    encoded_df = df.copy()
    for column in encoded_df.columns:
        if column != 'age':  # Exclude 'age' column from label encoding
            encoded_df[column] = le.fit_transform(encoded_df[column])
    return encoded_df

encoded_df = label_encode_dataframe(df)

print(encoded_df)

x = encoded_df.drop(columns=['treatment']);
y = encoded_df['treatment']


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
dt_model = DecisionTreeClassifier(max_depth=2,min_samples_split=4,min_samples_leaf=5)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)
print("Decision Tree Accuracy:", dt_accuracy)
dt_train_predictions = dt_model.predict(X_train)
dt_train_accuracy = accuracy_score(y_train, dt_train_predictions)
print("Accuracy on training data:", dt_train_accuracy)
pickle.dump(dt_model,open('Model.pkl','wb'))
os.getcwd()