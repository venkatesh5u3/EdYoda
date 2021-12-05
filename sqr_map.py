#!/usr/bin/env python
# coding: utf-8

# In[5]:


def triple(n):
    return n**2
my_list = [4, 5, 2, 9]
result = list(map(triple,my_list))
print(result)

