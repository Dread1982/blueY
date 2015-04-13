
# coding: utf-8

# In[1]:

import pandas as pd


# In[3]:

import numpy as np


# In[4]:

import matplotlib.pyplot as plt


# In[5]:

s = pd.Series([1,3,4,np.nan,6,8])


# In[6]:

s


# In[7]:

dates = pd.date_range('20130101',periods=6)


# In[8]:

dates


# In[9]:

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))


# In[10]:

df


# In[13]:

df2 = pd.DataFrame({'A':1.,'B':pd.Timestamp('20130102'),'C':pd.Series(1,index=list(range(4)),dtype='float32'),'D':np.array([3]*4,dtype='int32'),'E':pd.Categorical(["test","train","test","train"]),'F':'foo'})


# In[14]:

df2


# In[16]:

df2.E


# In[17]:

df.head()


# In[19]:

df.tail(2)


# In[20]:

df.index


# In[21]:

df.columns


# In[22]:

df.values


# In[23]:

df.describe()


# In[24]:

df.T


# In[26]:

df


# In[25]:

df['A']


# In[27]:

df[0:3]


# In[29]:

df.loc[:,['A','B']]


# In[30]:

df.loc['20130102',['A','B']]


# In[31]:

df.at[dates[0],'A']


# In[32]:

df.iloc[3]


# In[33]:

df.iloc[3:5,0:2]


# In[34]:

df.iloc[[1,2,4],[0,2]]


# In[35]:

df.iloc[1:3,:]


# In[36]:

df.iloc[1,1]


# In[37]:

df.iat[1,1]


# In[38]:

df[df.A > 0]


# In[39]:

df[df > 0]


# In[40]:

df2 = df.copy()


# In[41]:

df2['E']=['one', 'one','two','three','four','three']


# In[42]:

df2


# In[43]:

df2[df2['E'].isin(['two','four'])]


# In[44]:

s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))


# In[45]:

s1


# In[46]:

df.at[dates[0],'A'] = 0


# In[47]:

df


# In[48]:

df.iat[0,1] = 0


# In[49]:

df


# In[50]:

df.loc[:,'D'] = np.array([5] * len(df))


# In[51]:

df


# In[52]:

df['F'] = s1


# In[53]:

df


# In[54]:

df2 = df.copy()


# In[55]:

-df2


# In[56]:

df1.dropna(how='any')


# In[57]:

df.dropna(how='any')


# In[58]:

df


# In[60]:

df.fillna(value=5)


# In[61]:

pd.isnull(df)


# In[62]:

df.mean()


# In[63]:

df.mean(1)


# In[64]:

df.apply(lambda x: x.max() - x.min())


# In[65]:

df.apply(np.cumsum)


# In[66]:

s = pd.Series(np.random.randint(0,7,size=10))


# In[67]:

s


# In[68]:

s.value_counts()


# In[69]:

df = pd.DataFrame(np.random.randn(10, 4))


# In[70]:

df


# In[71]:

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})


# In[72]:

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})


# In[73]:

left


# In[74]:

right


# In[75]:

pd.merge(left, right, on='key')


# In[4]:

df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})


# In[1]:

import pandas as pd


# In[2]:

pd.__version__


# In[6]:

df


# In[5]:

df["grade"] = df["raw_grade"].astype("category")


# In[7]:

df


# In[8]:

df["grade"]


# In[10]:

df["grade"].cat.categories = ["very good", "good", "very bad"]


# In[11]:

df


# In[12]:

df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])


# In[13]:

df["grade"]


# In[15]:

import numpy as np


# In[16]:

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))


# In[17]:

ts = ts.cumsum()


# In[18]:

ts.plot()


# In[21]:

get_ipython().magic(u'matplotlib inline')


# In[22]:

ts.plot()


# In[23]:

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,columns=['A', 'B', 'C', 'D'])


# In[24]:

df = df.cumsum()


# In[27]:

import matplotlib.pyplot as plt


# In[28]:

plt.figure(); df.plot(); plt.legend(loc='best')


# In[ ]:



