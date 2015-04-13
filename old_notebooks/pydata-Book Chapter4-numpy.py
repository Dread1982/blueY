
# coding: utf-8

# In[2]:

import numpy as np


# In[11]:

data1 = [6,7.5,8,0,1]


# In[12]:

get_ipython().magic(u'pinfo data1')


# In[13]:

arr1 = np.array(data1)


# In[8]:

arr1.ndim


# In[14]:

arr1.shape


# In[15]:

arr1.dtype


# In[16]:

np.zeros(10)


# In[18]:

np.zeros((3,6))


# In[19]:

np.empty((2,3,2))


# In[21]:

np.arange(1,12,2)


# In[22]:

arr2 = np.array([1,2,3], dtype=np.float64)


# In[23]:

arr2.dtype


# In[24]:

arr1.dtype


# In[25]:

arr = np.array([1,2,3,4,5])


# In[26]:

arr.dtype


# In[28]:

float_arr = arr.astype(np.float64)


# In[29]:

float_arr.dtype


# In[34]:

numeric_strings = np.array(['1.23','-4.56'], dtype=np.string_)


# In[35]:

numeric_strings.dtype


# In[36]:

numeric_strings.astype(np.float64)


# In[39]:

arr = np.array([[1.,2.,3.],[1.,2.,3.]])


# In[40]:

arr


# In[41]:

arr * arr


# In[43]:

arr**0.5


# In[44]:

1 / arr


# In[45]:

arr = np.arange(1,10)


# In[46]:

arr


# In[47]:

arr[5:7] = 33


# In[48]:

arr


# In[50]:

arr_slice = arr[5:7]


# In[52]:

arr_slice[0] = 12


# In[53]:

arr


# In[54]:

arr2d = np.array([[1.,2.,3.],[4.,5.,6.]])


# In[55]:

arr2d


# In[59]:

arr2d[:2,:1]


# In[61]:

import numpy as np


# In[64]:

data = np.random.randn(7,4)


# In[65]:

data


# In[66]:

data[data < 0] = 0


# In[67]:

data


# In[68]:

arr = np.arange(32).reshape((8,4))


# In[69]:

arr


# In[71]:

arr[[1,5,7,2],[0,3,1,2]]


# In[72]:

arr[np.ix_([1,5,7,2],[0,3,2,1])]


# In[73]:

arr.T


# In[74]:

np.dot(arr.T,arr)


# In[75]:

arr = np.arange(10)


# In[76]:

np.sqrt(arr)


# In[77]:

np.exp(arr)


# In[78]:

np.pi


# In[79]:

points = np.arange(-5,5,0.01)


# In[80]:

xs, ys = np.meshgrid(points,points)


# In[81]:

ys


# In[82]:

import matplotlib.pyplot as plt


# In[83]:

z = np.sqrt(xs ** 2, ys ** 2)


# In[84]:

z


# In[89]:

plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()


# In[1]:

get_ipython().magic(u'matplotlib inline')


# In[90]:

plt.title=("Image plot of $\sqrt{x^2 + y^2}$ for a grid of valus")


# In[91]:

plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()


# In[3]:

xarr = np.array([1.1,1.2,1.3,1.4,1.5])


# In[4]:

yarr = np.array([2.1,2.2,2.3,2.4,2.5])


# In[5]:

cond = np.array([True, False,True,True,False])


# In[6]:

result = [(x if c else y) for x,y,c in  zip(xarr,yarr,cond)]


# In[7]:

result


# In[8]:

result = np.where(cond, xarr,yarr)


# In[9]:

result


# In[15]:

arr = np.random.randn(4,4)


# In[16]:

arr


# In[17]:

np.where(arr > 0, 2, -2)


# In[19]:

np.where(arr > 0, 2, arr)


# In[22]:

arr = np.random.randn(5,4)


# In[26]:

arr


# In[23]:

arr.mean()


# In[24]:

np.mean(arr)


# In[25]:

arr.sum()


# In[27]:

arr.mean(axis=1)


# In[28]:

arr.sum(0)


# In[30]:

arr = np.array([[0,1,2],[3,4,5],[6,7,8]])


# In[31]:

arr.cumsum(0)


# In[32]:

arr.cumprod(1)


# In[33]:

arr.std()


# In[34]:

arr.var()


# In[37]:

arr = np.random.randn(100)


# In[38]:

(arr>0).sum()


# In[39]:

bools = np.array([True, False,True])


# In[40]:

bools.any()


# In[41]:

bools.all()


# In[44]:

import numpy.random


# In[46]:

arr = np.random.randn(8)


# In[47]:

arr


# In[48]:

arr.sort()


# In[49]:

arr


# In[50]:

arr = np.random.randn(5,3)


# In[51]:

arr


# In[52]:

arr.sort(1)


# In[53]:

arr


# In[54]:

large_arr = np.random.randn(1000)


# In[55]:

large_arr.sort()


# In[57]:

large_arr[int(0.05 * len(large_arr))]  # 5% quantile


# In[ ]:



