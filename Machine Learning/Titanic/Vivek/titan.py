import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold, learning_curve
traindata = pd.read_csv('train.csv')
testdata = pd.read_csv('test.csv')
dataset = pd.concat([traindata, testdata], ignore_index=True, sort  = False)
dataset.info()
print(dataset[["Pclass","Survived"]].groupby(["Pclass"], as_index = False).mean())
print(dataset[["Sex","Survived"]].groupby(["Sex"],as_index = False).mean())
traindata['family'] = traindata['SibSp']+traindata['Parch']+1
testdata['family'] = testdata['SibSp']+testdata['Parch']+1
print(dataset[["family","Survived"]].groupby(["family"],as_index = False).mean())
print(dataset[["Embarked","Survived"]].groupby(["Embarked"],as_index = False).mean())
traindata['Embarked'] = traindata['Embarked'].fillna('S')
traindata.Age.fillna(traindata.Age.median(),inplace = True)
testdata.Age.fillna(testdata.Age.median(),inplace = True)
traindata.Fare.fillna(traindata.Fare.median(),inplace = True)
testdata.Fare.fillna(testdata.Fare.median(),inplace=True)
sexmap = {'female':0, 'male':1}
traindata['Sex'] = traindata['Sex'].map(sexmap).astype(int)
testdata['Sex'] = testdata['Sex'].map(sexmap).astype(int)
embarkmap = {'S':0, 'Q':1, 'C':2}
traindata['Embarked'] = traindata['Embarked'].map(embarkmap).astype(int)
testdata['Embarked'] = testdata['Embarked'].map(embarkmap).astype(int)
drope=["Name","Ticket","Cabin","SibSp","Parch","PassengerId"]
dropt=["Name","Ticket","Cabin","SibSp","Parch"]
traindata = traindata.drop(drope,axis=1)
testdata = testdata.drop(dropt,axis=1)
X_train = traindata.drop("Survived",axis=1)
y_train = traindata["Survived"]
X_test = testdata.drop("PassengerId",axis=1).copy()
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
print(repr(round(classifier.score(X_train, y_train) * 100, 2)))
submission = pd.DataFrame({'PassengerId': testdata['PassengerId'], 'Survived': y_pred})
submission = pd.DataFrame({
    "PassengerId": testdata["PassengerId"],
    "Survived": y_pred
})
submission.to_csv('submission.csv', index = False)


