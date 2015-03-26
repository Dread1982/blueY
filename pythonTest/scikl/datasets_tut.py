'''
Created on Mar 26, 2015

@author: manuel
'''
from sklearn import datasets
import pylab as pl

if __name__ == '__main__':
    iris = datasets.load_iris()
    data = iris.data
    print (data.shape)

    digits = datasets.load_digits()
    print (digits.images.shape)

   # pl.imshow(digits.images[-1], cmap=pl.cm.gray_r)  # using notebook now
