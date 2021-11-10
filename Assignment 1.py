#!/usr/bin/env python
# coding: utf-8

# # Importing necessary libraries

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
from sklearn import metrics
sns.set()


# # Reading the dataset

# In[27]:


df = pd.read_excel (r'C:\Users\HP\OneDrive\Desktop\iris.xls')
print(df)


# # Displaying the columns in the dataset

# In[4]:


df.columns


# # Calculating mean of each column

# In[29]:


df.mean(axis=0)


# # Checking for the null values

# In[30]:


df.isnull()


# # Data Visualization

# In[44]:


df.plot()


# In[14]:


df.plot.hist()


# In[46]:


df.plot.box()

