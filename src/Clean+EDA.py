#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import gzip
from pandas import DataFrame
from scipy.stats import uniform
from scipy.stats import randint
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def read_gz(gz):
    with gzip.open(str(gz)) as f:
        features_train = pd.read_csv(f, sep='\t')
    return features_train


# In[3]:


def clean_df(source):
    source = source.drop(['hm_beta','hm_odds_ratio','hm_ci_lower','hm_ci_upper','standard_error','ci_lower','odds_ratio','beta','ci_upper'],axis=1)
    source = source.dropna()
    return source


# In[4]:


def create_histogram(source,nbins):
    return source['p_value'].hist(bins=nbins)


# In[5]:


def manhattan_plot(source, height):
    plot_one = source[['p_value','chromosome']]
    plot_one['minuslog10pvalue'] = -np.log10(plot_one.p_value)
    plot_one.chromosome = plot_one.chromosome.astype('category')
    plot_one = plot_one.sort_values('chromosome')
    plot_one['ind'] = range(len(plot_one))
    plot_one_grouped = plot_one.groupby(('chromosome'))
    fig = plt.figure(figsize=(20,5))
    ax = fig.add_subplot(111)
    colors = ['red','green','blue', 'yellow']
    x_labels = []
    x_labels_pos = []
    for num, (name, group) in enumerate(plot_one_grouped):
        group.plot(kind='scatter', x='ind', y='minuslog10pvalue',color=colors[num % len(colors)], ax=ax)
        x_labels.append(name)
        x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
    ax.set_xticks(x_labels_pos)
    ax.set_xticklabels(x_labels)
    ax.set_xlim([0, len(plot_one)])
    ax.set_ylim([0, height])
    ax.set_xlabel('Chromosome')


# In[ ]:





# In[ ]:




