# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:51:11 2022

@author: Usuario
"""
from duneanalytics import DuneAnalytics
import pandas as pd

# initialize client
dune = DuneAnalytics('username', 'password')

# try to login
dune.login()

# fetch token
dune.fetch_auth_token()

# fetch query result id using query id
# query id for any query can be found from the url of the query:
# for example: 
# https://dune.com/queries/4494/8769 => 4494
# https://dune.com/queries/3705/7192 => 3705
# https://dune.com/queries/3751/7276 => 3751

result_id = dune.query_result_id(query_id=946173)

#fetch query result
data = dune.query_result(result_id)

result_list = data['data']['get_result_by_result_id']
result_list_clean=[e['data'] for e in result_list ]
df = pd.DataFrame(result_list_clean)

df = df.set_index('time')
df = df.sort_index()

df.to_excel (r'directory\filename.xlsx', header=True) #specify directory to save file and file name



