#!/usr/bin/env python
# coding: utf-8

# # api_data_wrangling_mini_project
# 
# 

# In[1]:


# pip install python-dotenv


# In[2]:


# get api key from your .env file
import os
from dotenv import load_dotenv

load_dotenv()
#print(os.environ)
API_KEY = os.environ.get('NASDAQ_API_KEY')

print(API_KEY) 


# Carl Zeiss Meditec, stock ticker: AFX_X https://www.zeiss.com/meditec/int/home.html
# 

# Request packages: http://docs.python-requests.org/en/master/
# 
# 
# collections modules: https://pymotw.com/3/collections/

# In[3]:


# First, import the relevant modules

import requests
import collections
import json


# In[4]:


# Now, call the Nasdaq API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
API_KEY = "-wPgQ4QygpJWZygPsEZU"
r= requests.get("https://data.nasdaq.com/api/v3/datasets/WIKI/FB/data.json?api_key=-wPgQ4QygpJWZygPsEZU")

#if(r.status_code == 200):
print(r.json())


# In[5]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure

result = r.json()
result.keys()


# In[6]:


result['dataset_data'].keys()


# In[ ]:





# In[ ]:




