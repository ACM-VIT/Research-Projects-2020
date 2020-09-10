
# :black_joker: Blackjack Win/Loss Predictor

Given the sum of cards of a player in Blackjack, the model predicts the outcome of the game with 69% accuracy.


![Alt Text](https://byandriykozachuk.files.wordpress.com/2018/09/blackjackml_big2.png?w=942)

## :gear: Implementation

A `RandomForestClassfier` was used to achieve the results with an accuracy of 69%. However, other two classification models that were tried and discard were:

Classifier | Accuracy
------------ | -------------
Gaussian Naive Bayes| 61%
Logistic Regression | 56%

```python
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'gini', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```

## :rocket: Results
The `Confusion Matrix` plotted below gives an estimate of the true positives and flase negatives to help evaluate the performance of the model.

```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred).round(2)
print(accuracy) 
``` 
![IMG](https://img.techpowerup.org/200408/figure-1.png)

## :page_facing_up: Dataset Source
>  [https://www.kaggle.com/mojocolors/900000-hands-of-blackjack-results](https://www.kaggle.com/mojocolors/900000-hands-of-blackjack-results)