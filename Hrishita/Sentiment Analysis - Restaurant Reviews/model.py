#Natural Language Processing

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3) #quoting = 3 means ignore double quotes in the file

#cleaning the text
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = [] #corpus means a collection of data that could mean anything
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review=review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set( stopwords.words('english'))] #converting the list of stopwords into a set makes the execution faster
    review= ' '.join(review)
    corpus.append(review)
    
#Creating the bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500) #keeps the 1500 most frequent words
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 0)

'''Naive Bayes'''
print("Naive Bayes: ")
# Fitting Naive Bayes classifier to the Training set
from sklearn.naive_bayes import GaussianNB
classifier_nb = GaussianNB()
classifier_nb.fit(X_train, y_train)

# Predicting the Test set results
y_pred_nb = classifier_nb.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(y_test, y_pred_nb)
print("Confusion Matrix: ")
print(cm_nb)

#Evaluation Methods (Precision (measuring exactness), Recall (measuring completeness) and the F1 Score (compromise between Precision and Recall)):
TP = cm_nb[1][1]
TN = cm_nb[0][0]
FP = cm_nb[0][1]
FN = cm_nb[1][0]
Accuracy_nb = (TP + TN) / (TP + TN + FP + FN)
Precision_nb = TP / (TP + FP)
Recall_nb = TP / (TP + FN)
F1Score_nb = 2 * Precision_nb * Recall_nb / (Precision_nb + Recall_nb) 
print("Accuracy: " + str(Accuracy_nb))
print("Precision: " + str(Precision_nb))
print("Recall: " + str(Recall_nb))
print("F1 Score: " + str(F1Score_nb))

'''Decision Tree'''
# Fitting Decision Tree classifier to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier_dt = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier_dt.fit(X_train, y_train)

# Predicting the Test set results
y_pred_dt = classifier_dt.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_dt = confusion_matrix(y_test, y_pred_dt)

#Evaluation Methods:
TP = cm_dt[1][1]
TN = cm_dt[0][0]
FP = cm_dt[0][1]
FN = cm_dt[1][0]
Accuracy_dt = (TP + TN) / (TP + TN + FP + FN)
Precision_dt = TP / (TP + FP)
Recall_dt = TP / (TP + FN)
F1Score_dt = 2 * Precision_dt * Recall_dt / (Precision_dt + Recall_dt) 

'''Random Forest'''
# Fitting Random Forest classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier_rf = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier_rf.fit(X_train, y_train)

# Predicting the Test set results
y_pred_rf = classifier_rf.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_rf = confusion_matrix(y_test, y_pred_rf)

#Evaluation Methods:
TP = cm_rf[1][1]
TN = cm_rf[0][0]
FP = cm_rf[0][1]
FN = cm_rf[1][0]
Accuracy_rf = (TP + TN) / (TP + TN + FP + FN)
Precision_rf = TP / (TP + FP)
Recall_rf = TP / (TP + FN)
F1Score_rf = 2 * Precision_rf * Recall_rf / (Precision_rf + Recall_rf) 
