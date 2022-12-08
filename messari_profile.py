# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:33:13 2022

@author: Usuario
"""

#profile data
import json
import pandas as pd
import urllib

url = "https://data.messari.io/api/v2/assets/aave/profile" 
req = urllib.request.Request(url)
req.add_header('x-messari-api-key', 'your api key') #change your api key for actual one
response = urllib.request.urlopen(req)
data = json.load(response)["data"]
    
df = pd.json_normalize(data, sep='_')
df.to_excel (r'directory\file_name.xlsx', header=True)
    
    
    
         