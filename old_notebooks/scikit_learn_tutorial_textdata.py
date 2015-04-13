
# coding: utf-8

# In[1]:

categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']


# In[2]:

from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train',
    categories=categories, shuffle=True, random_state=42)


# In[4]:

twenty_train.target_names


# In[6]:

len(twenty_train.data)


# In[7]:

len(twenty_train.filenames)


# In[8]:

print("\n".join(twenty_train.data[0].split("\n")[:3]))


# In[9]:

print(twenty_train.target_names[twenty_train.target[0]])


# In[10]:

twenty_train.target[:10]


# In[11]:

for t in twenty_train.target[:10]:
    print(twenty_train.target_names[t])


# In[12]:

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_train_counts.shape


# In[13]:

from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape


# In[14]:

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape


# In[15]:

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)


# In[16]:

docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))


# In[17]:

from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
])


# In[18]:

text_clf = text_clf.fit(twenty_train.data, twenty_train.target)


# In[19]:

import numpy as np
twenty_test = fetch_20newsgroups(subset='test',
    categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
np.mean(predicted == twenty_test.target)   


# In[20]:

from sklearn.linear_model import SGDClassifier
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5)),
])
_ = text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)
np.mean(predicted == twenty_test.target)   


# In[21]:

from sklearn import metrics
print(metrics.classification_report(twenty_test.target, predicted,
    target_names=twenty_test.target_names))
                                        










metrics.confusion_matrix(twenty_test.target, predicted)


# In[22]:

from sklearn.grid_search import GridSearchCV
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf__alpha': (1e-2, 1e-3),
}


# In[23]:

gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)


# In[24]:

gs_clf = gs_clf.fit(twenty_train.data[:400], twenty_train.target[:400])


# In[25]:

twenty_train.target_names[gs_clf.predict(['God is love'])]
'soc.religion.christian'


# In[26]:

best_parameters, score, _ = max(gs_clf.grid_scores_, key=lambda x: x[1])
for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, best_parameters[param_name]))





score        


# In[ ]:



