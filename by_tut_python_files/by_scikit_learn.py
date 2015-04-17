from __future__ import print_function, division
import sklearn.datasets
import sklearn.utils
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.grid_search import GridSearchCV


def get_dataset():
    # retrieving the boston data set; check out help(datasets.load_boston)
    boston = sklearn.datasets.load_boston()
    # shuffle the data set and get features X and target y
    X, y = sklearn.utils.shuffle(boston.data, boston.target, random_state=13)
    # make sure that all samples are floats
    X = X.astype(np.float64)
    return X, y


def split_into_train_and_test(X, y):
    split_idx = len(X) * 0.9
    X_train = X[:split_idx]
    X_test = X[split_idx:]
    y_train = y[:split_idx]
    y_test = y[split_idx:]
    return X_test, X_train, y_test, y_train


def get_mae_with_linear_regression(X, y):
    X_test, X_train, y_test, y_train = split_into_train_and_test(X, y)

    regr = linear_model.LinearRegression()

    regr.fit(X_train, y_train)

    pred = regr.predict(X_test)

    mae = np.mean(np.abs(pred - y_test))

    return mae


def get_mae_with_scale_and_linear_regression(X, y):
    X_test, X_train, y_test, y_train = split_into_train_and_test(X, y)

    pipe = Pipeline([('scale', preprocessing.StandardScaler()),
                     ('regr', linear_model.LinearRegression())])

    pipe.fit(X_train, y_train)

    pred = pipe.predict(X_test)

    mae = np.mean(np.abs(pred - y_test))

    return mae


def get_parameters_for_svr(X, y):
    X_test, X_train, y_test, y_train = split_into_train_and_test(X, y)

    params = dict(svr__gamma=[1e-2, 1e-3, 1e-4, 1e-5],
                  svr__C=[1, 10, 100, 1000, 10000])

    pipe = Pipeline([('scale', (preprocessing.StandardScaler())),
                     ('svr', svm.SVR())])

    clf = GridSearchCV(pipe, params, n_jobs=-1)

    clf.fit(X_train, y_train)

    best_parameters, score, _ = max(clf.grid_scores_, key=lambda x: x[1])
    for param_name in sorted(params.keys()):
        print("%s: %r" % (param_name, best_parameters[param_name]))


def get_mae_with_scale_and_svr(X, y):
    X_test, X_train, y_test, y_train = split_into_train_and_test(X, y)

    svr = svm.SVR(C=1000, gamma=0.01)

    pipe = Pipeline([('scale', preprocessing.StandardScaler()),
                    ('svr', svr)])

    pipe.fit(X_train, y_train)

    pred = pipe.predict(X_test)

    mae = np.mean(np.abs(pred - y_test))

    return mae

if __name__ == "__main__":
    X, y = get_dataset()
    print("lin reg: " + str(get_mae_with_linear_regression(X, y)))
    print("scale + lin reg: " + str(get_mae_with_scale_and_linear_regression(X, y)))

    # get_parameters_for_svr(X, y)
    print("scale + svr: " + str(get_mae_with_scale_and_svr(X, y)))