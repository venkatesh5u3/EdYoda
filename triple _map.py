#!/usr/bin/env python
# coding: utf-8

# In[4]:


def triple(n):
    return n*3
my_list = [1, 2, 3, 4, 5, 6, 7]
result = list(map(triple,my_list))
print(result)

