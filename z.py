#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#AIzaSyBilGA2PuhYUvetG-oymADy7RjC3gonEUg


# In[30]:


import pandas as pd


# In[ ]:


#UCqW8jxh4tH1Z1sWPbkGWL4g


# In[1]:


import googleapiclient.discovery


# In[2]:


channel_id=['UCqW8jxh4tH1Z1sWPbkGWL4g']


# In[3]:


api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBilGA2PuhYUvetG-oymADy7RjC3gonEUg"
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    


# In[4]:


request = youtube.channels().list(
        part="snippet,statistics",
        id="UCqW8jxh4tH1Z1sWPbkGWL4g"
    )
response = request.execute()

print(response)


# In[5]:


response


# In[7]:


title=response['items'][0]['snippet']['title']


# In[10]:


stat=response['items'][0]['statistics']['viewCount']


# In[11]:


subscriber=response['items'][0]['statistics']['subscriberCount']


# In[8]:


data=[]


# In[26]:


extract=dict(title=response['items'][0]['snippet']['title'],
             stat=response['items'][0]['statistics']['viewCount'],
            subscriber= response['items'][0]['statistics']['subscriberCount'])


# In[27]:


data.append(extract)


# In[9]:


data


# In[31]:


datanew=pd.DataFrame(data)


# In[32]:


datanew


# In[3]:


#pip install streamlit


# In[4]:


import streamlit as st


# In[10]:


st.dataframe(data)

