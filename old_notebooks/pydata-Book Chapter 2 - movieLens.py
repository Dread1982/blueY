
# coding: utf-8

# In[2]:

import pandas as pd


# In[29]:

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']


# In[30]:

users = pd.read_table('C:\Users\Manuel\Desktop\DataScience\pydata-book\pydata-book-master\ch02\movielens\users.dat', sep='::', header=None, names=unames)


# In[10]:

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']


# In[20]:

ratings = pd.read_table(r'C:\Users\Manuel\Desktop\DataScience\pydata-book\pydata-book-master\ch02\movielens\ratings.dat', sep='::', header=None, names=rnames)


# In[21]:

mnames = ['movie_id', 'title', 'genres']


# In[22]:

movies = pd.read_table(r'C:\Users\Manuel\Desktop\DataScience\pydata-book\pydata-book-master\ch02\movielens\movies.dat', sep='::', header=None, names=mnames)


# In[23]:

users[:5]


# In[24]:

ratings[:5]


# In[25]:

movies[:5]


# In[32]:

data = pd.merge(pd.merge(ratings,users),movies)


# In[34]:

data


# In[39]:

data.ix[0]


# In[41]:

mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')


# In[44]:

mean_ratings[:5]


# In[47]:

ratings_by_title = data.groupby('title').size()


# In[49]:

ratings_by_title[:10]


# In[50]:

active_titles = ratings_by_title.index[ratings_by_title >= 250]


# In[52]:

active_titles


# In[55]:

mean_ratings = mean_ratings.ix[active_titles]


# In[57]:

mean_ratings[:20]


# In[60]:

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)


# In[63]:

top_female_ratings[:10]


# In[64]:

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']


# In[65]:

sorted_by_diff = mean_ratings.sort_index(by='diff')


# In[66]:

sorted_by_diff[:15]


# In[67]:

sorted_by_diff[::-1][:15]


# In[69]:

rating_std_by_title = data.groupby('title')['rating'].std()


# In[70]:

rating_std_by_title = rating_std_by_title.ix[active_titles]


# In[71]:

rating_std_by_title.order(ascending=False)[:10]

