# capstone-
youtube data harvesting
#!/usr/bin/env python
# coding: utf-8

#AIzaSyBilGA2PuhYUvetG-oymADy7RjC3gonEUg
import pandas as pd
#UCqW8jxh4tH1Z1sWPbkGWL4g
import googleapiclient.discovery
channel_id=['UCqW8jxh4tH1Z1sWPbkGWL4g']
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBilGA2PuhYUvetG-oymADy7RjC3gonEUg"
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    
  request = youtube.channels().list(
        part="snippet,statistics",
        id="UCqW8jxh4tH1Z1sWPbkGWL4g"
    )
response = request.execute()

print(response)

response

title=response['items'][0]['snippet']['title']

stat=response['items'][0]['statistics']['viewCount']

subscriber=response['items'][0]['statistics']['subscriberCount']
data=[]
extract=dict(title=response['items'][0]['snippet']['title'],
             stat=response['items'][0]['statistics']['viewCount'],
            subscriber= response['items'][0]['statistics']['subscriberCount'])
data.append(extract)
data
datanew=pd.DataFrame(data)
datanew
#pip install streamlit
import streamlit as st
st.dataframe(data)

