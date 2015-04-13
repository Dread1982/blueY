
# coding: utf-8

# In[5]:

import pandas as pd


# In[5]:

names1880 = pd.read_csv(r'C:\Users\Manuel\Desktop\DataScience\pydata-book\pydata-book-master\ch02\names\yob1880.txt',names=['name','sex','births'])


# In[7]:

names1880


# In[12]:

names1880.groupby('sex').births.sum()


# In[10]:

years = range(1880,2011)


# In[7]:

pieces = []


# In[8]:

columns = ['name', 'sex', 'births']


# In[11]:

for year in years:
    path = r'C:\Users\Manuel\Desktop\DataScience\pydata-book\pydata-book-master\ch02\names\yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)


# In[12]:

names = pd.concat(pieces, ignore_index=True)


# In[13]:

names


# In[21]:

total_births = names.pivot_table('births',rows='year', cols='sex',aggfunc=sum)


# In[22]:

total_births.tail()


# In[24]:

get_ipython().magic(u'matplotlib inline')


# In[26]:

total_births.plot(title='Total birth by sex and year')


# In[1]:

def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


# In[16]:

names = names.groupby(['year','sex']).apply(add_prop)


# In[17]:

names


# In[20]:

import numpy as np


# In[21]:

np.allclose(names.groupby(['year','sex']).prop.sum(),1)


# In[22]:

def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]


# In[23]:

grouped = names.groupby(['year','sex'])


# In[24]:

top1000 = grouped.apply(get_top1000)


# In[25]:

top1000


# In[26]:

boys = top1000[top1000.sex == 'M']


# In[27]:

girls = top1000[top1000.sex == 'F']


# In[28]:

total_births = top1000.pivot_table('births',rows='year',cols='name', aggfunc=sum)


# In[29]:

total_births


# In[30]:

subset = total_births[['John','Harry','Mary','Marilyn']]


# In[33]:

subset.plot(subplots=True, figsize=(12,10),grid=False,title='Number of births per year')


# In[32]:

get_ipython().magic(u'matplotlib inline')


# In[37]:

table = top1000.pivot_table('prop',rows='year',cols='sex',aggfunc=sum)


# In[38]:

table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0,1.2,13), xticks=range(1880,2020,10))


# In[35]:

df = boys[boys.year == 2010]


# In[36]:

df


# In[58]:

prop_cumsum = df.sort_index(by='prop',ascending=False).prop.cumsum()


# In[60]:

prop_cumsum[:10]


# In[62]:

df = boys[boys.year == 1900]


# In[63]:

in1900 = df.sort_index(by='prop',ascending=False).prop.cumsum()


# In[64]:

# extract last letter from name column
get_last_letter = lambda x: x[-1]


# In[65]:

last_letters = names.name.map(get_last_letter)


# In[66]:

last_letters.name = 'last_letter'


# In[67]:

table = names.pivot_table('births',rows=last_letters,cols=['sex','year'],aggfunc=sum)


# In[68]:

subtable = table.reindex(columns=[1910,1960,2010],level='year')


# In[69]:

subtable.head()


# In[70]:

subtable.sum()


# In[71]:

letter_prop = subtable / subtable.sum().astype(float)


# In[74]:

import matplotlib.pyplot as plt


# In[75]:

fig, axis = plt.subplots(2,1,figsize=(10,8))


# In[80]:

letter_prop['M'].plot(kind='bar',rot=0,ax=axis[0],title='Male')


# In[79]:

get_ipython().magic(u'matplotlib inline')


# In[82]:

letter_prop['F'].plot(kind='bar', rot=0,ax=axis[1],title='Female',legend=False)


# In[83]:

letter_prop = table = table / table.sum().astype(float)


# In[84]:

dny_ts = letter_prop.ix[['d','n','y'],'M'].T


# In[85]:

dny_ts.head()


# In[86]:

dny_ts.plot()


# In[87]:

all_names = top1000.name.unique()


# In[89]:

mask = np.array(['lesl' in x.lower() for x in all_names])


# In[90]:

lesley_like = all_names[mask]


# In[91]:

lesley_like


# In[92]:

filtered = top1000[top1000.name.isin(lesley_like)]


# In[93]:

filtered.groupby('name').births.sum()


# In[94]:

table = filtered.pivot_table('births',rows='year',cols='sex',aggfunc=sum)


# In[95]:

table = table.div(table.sum(1),axis=0)


# In[96]:

table.tail()


# In[97]:

table.plot(style={'M': 'k-', 'F': 'k--'})


# In[98]:



