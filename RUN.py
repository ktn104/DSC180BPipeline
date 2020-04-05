#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.insert(0, 'src')
import wget
import pandas as pd
import os 
from ETL import get_data
from ETL import rename_data
from ETL import clean_data


def main(targets):

    if 'data' in targets:
        get_data()

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)






