'''
Created on Mar 26, 2015

@author: manuel
'''

from sklearn import datasets
from sklearn import svm


if __name__ == '__main__':
    iris = datasets.load_iris()
    digits = datasets.load_digits()

    # print(digits.data)
    # print(digits.target)

    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    predict = clf.predict(digits.data[-1])
    print(predict)
