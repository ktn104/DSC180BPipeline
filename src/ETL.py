#!/usr/bin/env python
# coding: utf-8

# In[39]:


import wget
import pandas as pd
import os 


# In[40]:


def get_data():
    url = 'https://www.ebi.ac.uk/gwas/api/search/downloads/alternative'
    wget.download(url)
    print('Finish getting data')


# In[41]:


def rename_data():
    os.rename(r'alternative',r'alternative.csv')


# In[43]:


get_data()
rename_data()


# In[44]:


def clean_data():
    df = pd.read_csv('alternative.csv', sep='\t')
    df = df[df['DISEASE/TRAIT'].str.contains("Type 2")]
    return df


# In[47]:


df


# In[ ]:





# In[ ]:




