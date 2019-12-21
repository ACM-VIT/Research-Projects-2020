#Artificial Neural Network

#Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder() #labelencoder encodes the strings randomly
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1]) #onehotencoder creates dummy variables
X = onehotencoder.fit_transform(X).toarray()
X = X[:,1:] #avoiding dummy variabe trap for countries
#gender has only two categories and so we don't need to make dummy variables as to avoid dummy varaible trap we will reduce it to one column which will basically give us back the same orginal column

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling - compulsory
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Part 2 - Creating the ANN

#importing the Keras libraries and packages
import keras
from keras.models import Sequential #for initialising the ANN
from keras.layers import Dense #forcreating the layers in the ANNs

#Initialising the ANN
classifier = Sequential()

#Adding input layer and the first hidden layer
classifier.add(Dense(activation="relu", input_dim=11, units=6, kernel_initializer="uniform")) #activation = "relu": rectifier activation, units: number of nodes in layer (tip-> (input nodes+output nodes)/2), input_dim : number of input nodes (to be mentioned only while initialising the first hidden layer), kernel_initializer = "uniform": initializes all weights on a uniform distribution and the values being close to 0

#Adding the second hidden layer
classifier.add(Dense(activation="relu", units=6, kernel_initializer="uniform"))

#Adding the output layer
classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform")) #our output is a yes or no and so we want a probability of yes or no and hence we use sigmoid, if the output had more than 2 categories then units = no_of_categories and activation = "softmax"

#Compiling the ANN - applying the stochastic gradient descent to the ANN
classifier.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"]) #metrics decides on what list of parameters will they update the weights of the ANN
#loss is basically the cost function: since our output is binary and the activation function is sigmoid the model is almost like logistic regression which has a loss function = logarithmic loss so we use binary_crossentropy if there were more than 2 categories it would be categorical_crossentropy

#Fitting the ANN to the training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100) #epochs is the number of time the ANN will train over the training set

#Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred>0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)