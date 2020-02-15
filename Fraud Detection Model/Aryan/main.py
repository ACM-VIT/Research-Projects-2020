
import pandas as pd

# Read the CSV file
data = pd.read_csv('creditcard2.csv')
# Show the contents
print(data)
#Drop the unnecessary columns
data=data.drop(['nameOrig','nameDest'], axis=1)

# label encoding the data 
from sklearn.preprocessing import LabelEncoder   
le = LabelEncoder()   
data['type']= le.fit_transform(data['type']) 

# importing one hot encoder from sklearn 
from sklearn.preprocessing import OneHotEncoder   
# creating one hot encoder object with categorical feature 0 
# indicating the first column 
onehotencoder = OneHotEncoder(categorical_features = [0]) 
data = onehotencoder.fit_transform(data).toarray()
print(data)
