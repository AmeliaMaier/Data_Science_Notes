from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

def k_fold_example(x, y):
    kfold = KFold(3, shuffle=True)
    x = x.values
    y = y.values
    accuracies = []
    precisions = []
    recalls = []
    kfold.get_n_splits(x)

    for train_index, test_index in kfold.split(x):
        model = LogisticRegression()
        model.fit(x[train_index], y[train_index])
        y_predict = model.predict(x[test_index])
        y_true = y[test_index]
        accuracies.append(accuracy_score(y_true, y_predict))
        precisions.append(precision_score(y_true, y_predict))
        recalls.append(recall_score(y_true, y_predict))
    print(np.average(accuracies))
    print(np.average(precisions))
    print(np.average(recalls))


y = data_df['admit']
x = pd.get_dummies(data_df.drop('admit', axis=1), columns=['rank'])
k_fold_example(x,y)
filename = './data/grad.csv'
data_df = pd.read_csv(filename)
