#!/usr/bin/env python
# coding: utf-8

# In[4]:


def check_palindrome(string):
    start = 0
    end = len(string)-1
    while start < end:
        c1 = string[start]
        c2 = string[end]
        if c1 != c2:
            return False
        else:
            start+=1
            end-=1
    return True


# In[16]:


string = '1anna1'


# In[17]:


check_palindrome(string)


# In[18]:


def isPalindrome(s):
    return s == s[::-1]


# In[19]:


isPalindrome(string)


# In[ ]:




