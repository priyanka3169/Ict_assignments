#!/usr/bin/env python
# coding: utf-8

# # Importing necessary libraries

# In[34]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # 1. Reading the dataset 

# In[35]:


df=pd.read_csv("cars_data.csv")
df


# # 2.Checking for null values

# In[36]:


df.isnull().sum()


# # Counting the number of male and female customers

# In[37]:


gender=df['Buyer Gender'].value_counts()


# # 3.Bar graph of male vs female buyers

# In[38]:


fig = plt.figure(figsize = (5, 5))
gender.plot.bar(title='Male vs Female buyers')
plt.xlabel("Gender")
plt.ylabel("Number of People")


# # 4.Top 5 cars based on their sales price.

# In[29]:


sorted_salesprice = df.sort_values(['Sale Price'], ascending=False)


# In[39]:


top_five = sorted_salesprice[['Make','Model','Sale Price']].head()
top_five


# # 5.Least 5 cars based on their Resell price.
# 

# In[31]:


sorted_resellprice =  df.sort_values(['Resell Price'], ascending= True)


# In[32]:


least_five = sorted_resellprice[['Make','Model','Resell Price']].head()
least_five

