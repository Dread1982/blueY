'''
Created on Mar 30, 2015

@author: manuel



'''

import numpy as np
import requests
from StringIO import StringIO
from blaze.server.server import dataset
from sklearn import preprocessing
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Ridge
from sklearn.grid_search import GridSearchCV
from scipy.stats import uniform as sp_rand
from sklearn.grid_search import RandomizedSearchCV

# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"


def normalize_and_standardize(X):
    # normalize the data attributes
    normalized_X = preprocessing.normalize(X)
    # standardize the data attributes
    standardized_X = preprocessing.scale(X)


def feature_selection(X, y):
    model = ExtraTreesClassifier()
    model.fit(X, y)  # display the relative importance of each attribute
    print model.feature_importances_

    model = LogisticRegression()
    # create the RFE model and select 3 attributes
    rfe = RFE(model, 3)
    rfe.fit(X, y)
    # summarize the selection of the attributes
    print(rfe.support_)
    print(rfe.ranking_)


def download_and_load_data(data_url):
    # download the file
    resp = requests.get(data_url)
    if resp.status_code == 200:
        # load the CSV file as a numpy matrix
        dataset = np.loadtxt(StringIO(resp.content), delimiter=",")
        return dataset


def algorithm_development(X, y):
    #model = LogisticRegression()
    #model = GaussianNB()
    #model = KNeighborsClassifier()
    #model = DecisionTreeClassifier()
    model = SVC()

    model.fit(X, y)
    print model  # make predictions
    expected = y
    predicted = model.predict(X)  # summarize the fit of the model
    print metrics.classification_report(expected, predicted)
    print metrics.confusion_matrix(expected, predicted)


def optimize_algorithm_parameters(X, y):
    # prepare a range of alpha values to test
    alphas = np.array([1, 0.1, 0.01, 0.001, 0.0001, 0])
    # create and fit a ridge regression model, testing each alpha
    model = Ridge()
    grid = GridSearchCV(estimator=model, param_grid=dict(alpha=alphas))
    grid.fit(X, y)
    print(grid)
    # summarize the results of the grid search
    print(grid.best_score_)
    print(grid.best_estimator_.alpha)

    # prepare a uniform distribution to sample for the alpha parameter
    param_grid = {'alpha': sp_rand()}
    # create and fit a ridge regression model, testing random alpha values
    model = Ridge()
    rsearch = RandomizedSearchCV(
        estimator=model, param_distributions=param_grid, n_iter=100)
    rsearch.fit(X, y)
    print(rsearch)
    # summarize the results of the random parameter search
    print(rsearch.best_score_)
    print(rsearch.best_estimator_.alpha)

if __name__ == '__main__':
    dataset = download_and_load_data(url)

    # separate the data from the target attributes
    X = dataset[:, 0:7]
    y = dataset[:, 8]

    optimize_algorithm_parameters(X, y)
