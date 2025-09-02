#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.read_csv(r"C:\Users\jason\Downloads\dirty_cafe_sales.csv")


# In[22]:


df.head(50)
df=df.replace('UNKNOWN', '')
df=df.replace('ERROR', '')
df=df.fillna('')


# In[23]:


df.head(20)


# In[ ]:




