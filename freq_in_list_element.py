#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = ['a','b','c', 'a', 'c', 'a', 'a', 'c', 'd', 'e']


# In[12]:


frequency = {}
for item in list:
    if (item in frequency):
        frequency[item] += 1
    else:
        frequency[item] = 1


# In[13]:


frequency


# In[14]:


freq = {} 
for items in list: 
    freq[items] = d.count(items) 


# In[15]:


freq


# In[16]:


from collections import Counter


# In[17]:


Counter(list)


# In[2]:


x = "saurabh sharma"


# In[6]:


f = {}
m = []


# In[13]:


for a in [j for i in x.split() for j in i]:
    if a in f:
        f[a] +=1
    else:
        f[a] = 1


# In[14]:


f


# In[ ]:




