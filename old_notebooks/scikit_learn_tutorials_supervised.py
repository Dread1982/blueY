
# coding: utf-8

# In[1]:

import pylab as pl


# In[2]:

pl.cm.gray_r


# In[3]:

from sklearn import datasets


# In[4]:

digits = datasets.load_digits()


# In[63]:

pl.imshow(digits.images[-1], cmap=pl.cm.gray_r)


# In[57]:

get_ipython().magic(u'matplotlib inline')


# In[61]:

pl.imshow(digits.images[-1], cmap=pl.cm.gray_r)


# In[14]:

data = digits.images.reshape((digits.images.shape[0], -1))


# In[15]:

import numpy as np


# In[16]:

from sklearn import datasets


# In[17]:

iris = datasets.load_iris()


# In[18]:

iris_X = iris.data


# In[22]:

iris_y = iris.target


# In[23]:

np.unique(iris_y)


# In[28]:

np.random.seed(0)


# In[30]:

indices = np.random.permutation(len(iris_X))


# In[35]:

# Split iris data in train and test data
# A random permutation, to split the data randomly


# In[31]:

iris_X_train = iris_X[indices[:-10]]


# In[32]:

iris_y_train = iris_y[indices[:-10]]


# In[33]:

iris_X_test  = iris_X[indices[-10:]]


# In[34]:

iris_y_test  = iris_y[indices[-10:]]


# In[36]:

from sklearn.neighbors import KNeighborsClassifier


# In[37]:

knn = KNeighborsClassifier()


# In[38]:

knn.fit(iris_X_train, iris_y_train) 
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
               metric_params=None, n_neighbors=5, p=2, weights='uniform')


# In[39]:

knn.predict(iris_X_test)


# In[40]:

iris_y_test


# In[41]:

diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test  = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test  = diabetes.target[-20:]


# In[62]:

get_ipython().magic(u'doctest_mode')


# In[44]:

from sklearn import linear_model


# In[46]:

regr = linear_model.LinearRegression()


# In[48]:

regr.fit(diabetes_X_train, diabetes_y_train)


# In[49]:

print(regr.coef_)


# In[50]:

# The mean square error
np.mean((regr.predict(diabetes_X_test)-diabetes_y_test)**2)


# In[51]:

# Explained variance score: 1 is perfect prediction
# and 0 means that there is no linear relationship
# between X and Y.
regr.score(diabetes_X_test, diabetes_y_test) 


# In[64]:

X = np.c_[ .5, 1].T
y = [.5, 1]
test = np.c_[ 0, 2].T
regr = linear_model.LinearRegression()

import pylab as pl 
pl.figure() 

np.random.seed(0)
for _ in range(6): 
   this_X = .1*np.random.normal(size=(2, 1)) + X
   regr.fit(this_X, y)
   pl.plot(test, regr.predict(test)) 
   pl.scatter(this_X, y, s=3) 


# In[65]:

regr = linear_model.Ridge(alpha=.1)

pl.figure() 

np.random.seed(0)
for _ in range(6): 
   this_X = .1*np.random.normal(size=(2, 1)) + X
   regr.fit(this_X, y)
   pl.plot(test, regr.predict(test)) 
   pl.scatter(this_X, y, s=3) 


# In[66]:

alphas = np.logspace(-4, -1, 6)
from __future__ import print_function
print([regr.set_params(alpha=alpha
            ).fit(diabetes_X_train, diabetes_y_train,
            ).score(diabetes_X_test, diabetes_y_test) for alpha in alphas]) 


# In[67]:

regr = linear_model.Lasso()
scores = [regr.set_params(alpha=alpha
            ).fit(diabetes_X_train, diabetes_y_train
            ).score(diabetes_X_test, diabetes_y_test)
       for alpha in alphas]
best_alpha = alphas[scores.index(max(scores))]
regr.alpha = best_alpha
regr.fit(diabetes_X_train, diabetes_y_train)



print(regr.coef_)


# In[68]:

logistic = linear_model.LogisticRegression(C=1e5)
logistic.fit(iris_X_train, iris_y_train)




# In[69]:

from sklearn import svm
svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)   


# In[70]:

from sklearn import datasets, svm
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target
svc = svm.SVC(C=1, kernel='linear')
svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])


# In[71]:

import numpy as np
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)
scores = list()
for k in range(3):
    # We use 'list' to copy, in order to 'pop' later on
    X_train = list(X_folds)
    X_test  = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test  = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))
print(scores)


# In[72]:

from sklearn import cross_validation
k_fold = cross_validation.KFold(n=6, n_folds=3)
for train_indices, test_indices in k_fold:
     print('Train: %s | test: %s' % (train_indices, test_indices))


# In[73]:

kfold = cross_validation.KFold(len(X_digits), n_folds=3)
[svc.fit(X_digits[train], y_digits[train]).score(X_digits[test], y_digits[test])
         for train, test in kfold]


# In[74]:

cross_validation.cross_val_score(svc, X_digits, y_digits, cv=kfold, n_jobs=-1)


# In[75]:

from sklearn.grid_search import GridSearchCV
gammas = np.logspace(-6, -1, 10)
clf = GridSearchCV(estimator=svc, param_grid=dict(gamma=gammas),
                   n_jobs=-1)
clf.fit(X_digits[:1000], y_digits[:1000])        

clf.best_score_                                  

clf.best_estimator_.gamma == 1e-6


# Prediction performance on test set is not as good as on train set
clf.score(X_digits[1000:], y_digits[1000:])


# In[76]:

from sklearn import linear_model, datasets
lasso = linear_model.LassoCV()
diabetes = datasets.load_diabetes()
X_diabetes = diabetes.data
y_diabetes = diabetes.target
lasso.fit(X_diabetes, y_diabetes)



# The estimator chose automatically its lambda:
lasso.alpha_ 


# In[ ]:



