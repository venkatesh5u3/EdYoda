#!/usr/bin/env python
# coding: utf-8

# In[67]:


def noOfUpperLower(s):
    u=0
    l=0
    for i in s:
        i=ord(i)
        if i>=97 and i<=123:
            l+=1
        elif i>=65 and i<=91:
            u+=1
    print("No. of Upper case characters : ",u)
    print("No. of Lower case Characters : ",l)
noOfUpperLower('The quick Brow Fox')

