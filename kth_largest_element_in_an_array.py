#!/usr/bin/env python
# coding: utf-8

# In[9]:


l = [7,1,2,45,12,44,15,22,10]
k = 5


# In[12]:


sorted(l)


# In[11]:


len(l)-k


# In[10]:


sorted(l)[len(l)-k]


# In[17]:


from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    return sorted(nums)[len(nums)-k]


# In[18]:


findKthLargest(l, k)


# In[ ]:




