#!/usr/bin/env python
# coding: utf-8

# In[54]:


d = {"saurabh": 10, "pratyush": 50, "rahul": 200, "deepak": 150, "abhishek": 100}


# In[55]:


x = [(k,v) for k, v in sorted(d.items(), key = lambda item: item[1], reverse=True)]
x


# In[57]:


from collections import OrderedDict


# In[60]:


OrderedDict(x)

