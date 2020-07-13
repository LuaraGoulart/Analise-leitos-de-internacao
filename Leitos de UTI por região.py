#!/usr/bin/env python
# coding: utf-8

# <h1>Quantidade de Leitos de UTI por região</h1>
# 
# Análise feita para fins universitários, criado por <b>Luara C. Lopes Goulart</b> aluna da Faculdade de Tecnologia do Estado de São Paulo - FATEC SJC. Será apresentada uma análise com a quantidade de Leitos de UTI disponíveis nas regiões do Brasil, a partir dos dados encontrados<a href='https://saude-ibgedgc.hub.arcgis.com/datasets/2dfd385e7ded49c6b7f7929911806a20_7/data?geometry=-162.426%2C-41.782%2C59.585%2C15.270&orderBy=Leitos_UTI_Total&orderByAsc=false&where=Leitos_UTI_Total%20%3E%3D%200'>  neste dataset</a>. Com o intuito de visualizarmos a quantidade de leitos disponiveis nas UTIs, seja SUS ou não.

# In[1]:


import pandas as pd
low_memory=False
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90


# In[2]:


df = pd.read_csv('Leitos_de_UTI_em2019.csv')


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


df.sample(10)


# In[6]:


df.groupby('Nome_Estado')['Leitos_UTI_SUS_Total'].max().sort_values(ascending=False)


# In[7]:


df.groupby('Nome_Estado')['Leitos_UTI_SUS_Total'].max().sort_values().tail(27).plot(kind='barh', color='indianred')


# In[8]:


df.groupby('Nome_Estado')['Leitos_UTI_Total'].max().sort_values(ascending=False)


# In[9]:


df.groupby('Nome_Estado')['Leitos_UTI_Total'].max().sort_values().tail(27).plot(kind='bar', color='coral')


# In[ ]:




