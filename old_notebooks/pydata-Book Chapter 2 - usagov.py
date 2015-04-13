
# coding: utf-8

# In[1]:

path = 'C:\Users\Manuel\Desktop\DataScience\pydata-book\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'


# In[3]:

open(path).readline()


# In[4]:

import json


# In[5]:

records = [json.loads(line) for line in open(path)]


# In[11]:

records[0]


# In[12]:

records[0]['tz']


# In[30]:

time_zones = [rec['tz'] for rec in records if 'tz' in rec]


# In[31]:

time_zones[:10]


# In[35]:

def get_counts(sequence):
    counts = {}
    for s in sequence:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    return counts


# In[37]:

from collections import defaultdict


# In[46]:

def get_counts2(sequence):
    counts = defaultdict(int)
    for s in sequence:
        counts[s] += 1
    return counts


# In[48]:

get_counts(time_zones) == get_counts2(time_zones)


# In[43]:

len(time_zones)


# In[55]:

counts = get_counts2(time_zones)


# In[50]:

counts['America/New_York']


# In[56]:

counts


# In[54]:

len(counts)


# In[51]:

def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


# In[61]:

top_counts(counts)


# In[63]:

from collections import Counter


# In[64]:

counts = Counter(time_zones)


# In[65]:

counts.most_common(10)


# In[66]:

from pandas import DataFrame, Series


# In[67]:

import pandas as pd


# In[68]:

import numpy as np


# In[69]:

frame = DataFrame(records)


# In[70]:

frame


# In[76]:

tz_counts = frame['tz'].value_counts()


# In[77]:

tz_counts[:10]


# In[78]:

clean_tz = frame['tz'].fillna('Missing')


# In[79]:

clean_tz[clean_tz == ''] = 'Unknown'


# In[80]:

tz_counts = clean_tz.value_counts()


# In[81]:

tz_counts[:10]


# In[83]:

get_ipython().magic(u'matplotlib inline')


# In[87]:

tz_counts[:10].plot(kind = 'barh', rot =0)


# In[90]:

frame['a'][25]


# In[91]:

results = Series([x.split()[0] for x in frame.a.dropna()])


# In[92]:

results[:5]


# In[96]:

results.value_counts()[:8]


# In[100]:

cframe = frame[frame.a.notnull()]


# In[101]:

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')


# In[103]:

operating_system[:5]


# In[106]:

by_tz_os = cframe.groupby(['tz',operating_system])


# In[107]:

agg_counts = by_tz_os.size().unstack().fillna(0)


# In[108]:

agg_counts[:10]


# In[110]:

indexer = agg_counts.sum(1).argsort()


# In[111]:

indexer[:10]


# In[112]:

count_subset = agg_counts.take(indexer)[-10:]


# In[114]:

count_subset


# In[115]:

count_subset.plot(kind='barh',stacked=True)


# In[116]:

normed_subset = count_subset.div(count_subset.sum(1),axis=0)


# In[117]:

normed_subset.plot(kind='barh',stacked=True)


# In[ ]:



