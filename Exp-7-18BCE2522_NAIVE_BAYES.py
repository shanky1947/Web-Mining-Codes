from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# load the iris datasets
dataset = datasets.load_iris()
# fit a Naive Bayes model to the data

xtrain, xtest, ytrain, ytest=train_test_split(dataset.data, dataset.target)

model = GaussianNB()

model.fit(xtrain, ytrain)
print(model)

# make predictions
expected = ytest
predicted = model.predict(xtest)

# summarize the fit of the model
print(metrics.confusion_matrix(expected, predicted))




cf_matrix = metrics.confusion_matrix(expected, predicted)
print(cf_matrix)

import seaborn as sns
sns.heatmap(cf_matrix, annot=True)