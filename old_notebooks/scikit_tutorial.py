
# coding: utf-8

# In[1]:

from sklearn import datasets


# In[3]:

iris = datasets.load_iris()


# In[4]:

digits = datasets.load_digits()


# In[6]:

digits.data


# In[7]:

digits.target


# In[9]:

from sklearn import svm


# In[11]:

clf = svm.SVC(gamma=0.001, C=100.)


# In[12]:

clf.fit(digits.data[:-1], digits.target[:-1])


# In[13]:

clf.predict(digits.data[-1])


# In[15]:

from sklearn import svm


# In[16]:

from sklearn import datasets


# In[17]:

clf = svm.SVC()


# In[18]:

iris = datasets.load_iris()


# In[19]:

X,y = iris.data, iris.target


# In[20]:

clf.fit(X,y)


# In[21]:

import pickle


# In[22]:

s = pickle.dumps(clf)


# In[23]:

clf2 = pickle.loads(s)


# In[24]:

clf2.predict(X[0])


# In[25]:

y[0]


# In[26]:

from sklearn.externals import joblib


# In[27]:

joblib.dump(clf, 'filename.pkl')


# In[28]:

clf = joblib.load('filename.pkl')


# In[ ]:



