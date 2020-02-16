import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
dataset = pd.read_csv('diamonds.csv')
dataset.drop('Unnamed: 0', axis = 1, inplace = True)
X = dataset.drop('price', axis = 1)
y = dataset['price']
plt.figure(figsize=[12,12])
plt.subplot(221)
plt.hist(dataset['carat'],bins=20,color='lightseagreen')
plt.xlabel('Carat Weight')
plt.ylabel('Frequency')
plt.title('Distribution of Diamond Carat Weight')
plt.subplot(222)
plt.hist(dataset['depth'],bins=20,color='royalblue')
plt.xlabel('Diamond Depth (%)')
plt.ylabel('Frequency')
plt.title('Distribution of Diamond Depth')
plt.subplot(223)
plt.hist(dataset['price'],bins=20,color='salmon')
plt.xlabel('Price in USD')
plt.ylabel('Frequency')
plt.title('Distribution of Diamond Price')
plt.scatter(dataset['price'],dataset['carat'])
plt.figure(figsize=(10,8))
sns.heatmap(dataset.corr(),annot=True,cmap='YlGnBu')
fig, saxis = plt.subplots(2, 2,figsize=(12,12))
sns.regplot(x = 'carat', y = 'price', data=dataset, ax = saxis[0,0])
sns.regplot(x = 'x', y = 'price', data=dataset, ax = saxis[0,1])
sns.regplot(x = 'y', y = 'price', data=dataset, ax = saxis[1,0])
sns.regplot(x = 'z', y = 'price', data=dataset, ax = saxis[1,1])
sns.barplot(x = 'cut', y = 'price', order=['Fair','Good','Very Good','Premium','Ideal'], data=dataset)
sns.barplot(x = 'color', y = 'price', order=['J','I','H','G','F','E','D'], data=dataset)
sns.barplot(x = 'clarity', y = 'price', order=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF'], data=dataset)
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(), [1,2,3])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X), dtype = np.float)
X = X[:, 1:]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
from sklearn.metrics import r2_score
print(r2_score(y_test, y_pred)) 