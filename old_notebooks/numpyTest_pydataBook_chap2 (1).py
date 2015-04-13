
# coding: utf-8

# In[2]:

import numpy as np


# In[1]:

data1 = [6, 7.5, 8,0,1]


# In[2]:

data1


# In[3]:

type(data1)


# In[8]:

arr1 = np.array(data1)


# In[9]:

arr1


# In[10]:

type(arr1)


# In[11]:

arr1.dtype


# In[12]:

arr1.shape


# In[13]:

data2 = [[1,2,3,4],[5,6,7,8]]


# In[14]:

arr2 = np.array(data2)


# In[15]:

arr2


# In[16]:

arr2.shape


# In[17]:

arr2.dtype


# In[20]:

np.zeros((3,6))


# In[21]:

np.arange(10)


# In[22]:

np.ones(7)


# In[23]:

arr1 = np.array([1,2,3], dtype=np.float64)


# In[24]:

arr1.dtype


# In[26]:

arr2 = np.array([1,2,3], dtype=np.int32)


# In[27]:

arr2.dtype


# In[28]:

float_arr = arr2.astype(np.float64)


# In[29]:

float_arr.dtype


# In[31]:

numeric_strings = np.array(['1.3', '2.6', '-4.4'])


# In[32]:

str_as_float_arr = numeric_strings.astype(np.float64)


# In[35]:

str_as_float_arr


# In[36]:

str_as_float_arr.dtype


# In[40]:

arr = np.array([[1,2,3],[4,5,6]])


# In[41]:

arr


# In[39]:

arr * arr


# In[43]:

arr = arr.astype(np.float64)


# In[44]:

1/arr


# In[46]:

arr **3


# In[52]:

arr = np.arange(10)


# In[53]:

arr


# In[48]:

arr[5]


# In[49]:

arr[5:8]


# In[50]:

arr[5:8] = 12


# In[51]:

arr


# In[54]:

arr_slice = arr[5:8]


# In[55]:

arr_slice[1] = 12345


# In[56]:

arr_slice


# In[57]:

arr


# In[58]:

arr_slice[:] = 64


# In[89]:

arr   # slicing with index always creates a view


# In[60]:

arr_copy = arr[5:8].copy()


# In[62]:

arr_copy[1] = 0


# In[63]:

arr_copy


# In[64]:

arr


# In[65]:

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[66]:

arr2d


# In[67]:

arr2d[1]


# In[68]:

arr2d[1][0]


# In[69]:

arr2d[1,0]


# In[71]:

arr2d[:,0]


# In[73]:

arr2d[:2]


# In[74]:

arr2d[2:]


# In[78]:

arr2d[1:,0]


# In[79]:

arr2d[:,:1]


# In[80]:

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])


# In[101]:

data = np.random.randn(7,4)


# In[102]:

data


# In[84]:

names == 'Bob'


# In[103]:

data[names == 'Bob']


# In[104]:

data[names == 'Bob', :2]


# In[105]:

data[-(names == 'Bob')]  # negate


# In[106]:

bob_data = data[names == 'Bob'] 


# In[108]:

bob_data[1,:] = 7.7777


# In[109]:

bob_data


# In[110]:

data #slicing by boolean always creates a copy


# In[3]:

arr = np.empty((8,4))


# In[4]:

for i in range(8):
    arr[i] = i


# In[5]:

arr


# In[8]:

arr[[4,2]]


# In[9]:

arr = np.arange(32).reshape((8,4))


# In[10]:

arr


# In[11]:

arr[[1,5,7,2],[0,3,1,2]]


# In[13]:

arr = np.arange(15).reshape((3,5))


# In[14]:

arr


# In[15]:

arr.T


# In[16]:

arr = np.random.randn(6,3)


# In[17]:

arr


# In[18]:

np.dot(arr.T,arr)


# In[21]:

arr = np.arange(16).reshape((2,2,4))


# In[22]:

arr


# In[23]:

arr.transpose((1,0,2))


# In[24]:

arr = np.arange(10)


# In[25]:

arr


# In[26]:

np.sqrt(arr)


# In[27]:

arr = np.random.randn(4,4)


# In[28]:

arr


# In[29]:

np.where(arr > 0, 2, -2)


# In[30]:

arr.mean()


# In[31]:

arr.sum(0)


# In[32]:

arr.sum(1)


# In[33]:

arr.std()


# In[34]:

arr.var()


# In[37]:

bools = np.array([False, False,True,False])


# In[38]:

bools.any()


# In[39]:

bools.all()


# In[7]:

arr = np.random.randn(8)


# In[8]:

arr


# In[12]:

sort_arr = arr.sort()


# In[14]:

arr


# In[15]:

names = np.array(['a','b','c','a','b'])


# In[16]:

np.unique(names)


# In[17]:

# file in / out


# In[18]:

arr = np.arange(10)


# In[19]:

np.save('some_array',arr)


# In[21]:

np.load('some_array.npy')


# In[22]:

get_ipython().magic(u'timeit 4 +5')


# In[ ]:



