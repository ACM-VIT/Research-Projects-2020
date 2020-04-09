import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
# Importing the dataset
dataset = pd.read_csv('blkjckhands.csv')
blkjck_hnds = dataset[['sumofcards','winloss']].copy()
le = preprocessing.LabelEncoder()
blkjck_hnds['winloss'] = le.fit_transform(blkjck_hnds['winloss'])
X = blkjck_hnds.drop('winloss',axis=1).values
y = blkjck_hnds['winloss'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42, stratify=y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'gini', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred).round(2)
print(accuracy)

import scikitplot as skplt
skplt.metrics.plot_confusion_matrix(y_test, y_pred)
plt.show()
