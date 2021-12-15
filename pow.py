#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Power:
    def __init__(self, x,n):
        self.x = x
        self.n = n
    def pow_fun(self):
        print( self.x**self.n)
p = Power(int(input('x : ')),int(input('n : ')))
p.pow_fun()


# In[ ]:




