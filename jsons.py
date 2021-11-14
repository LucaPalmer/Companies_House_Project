# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import requests
import json
#import chwrapper
import pandas as pd
import os
import subprocess

os.chdir('/home/lucapalmer98/project/csvs')

filename = str(input('Enter a json filename to load (must end in .txt)'))
filepath = '/home/lucapalmer98/project/jsons/' + filename

print("Your filepath: ", filepath)

with open(filepath) as f:
    lines = f.readlines()

container = []
for x in range(len(lines)):
    container.append(json.loads(lines[x]))

# +
#jsons = pd.DataFrame(container)
#jsons = jsons['data']
# -

jsons = []
for x in range(len(container)):
    jsons.append(container[x]['data'])

jsons_df = pd.json_normalize(jsons)
jsons_df['sic_codes'] = jsons_df['sic_codes'].str[0]

jsons_df

# +
#jsons_df.iloc[1:3] # Get records by row number

# + tags=[]

column_names = list(jsons_df.columns)
column_pos = [jsons_df.columns.get_loc(c) for c in jsons_df.columns if c in jsons_df]

column_pos = dict(zip(column_pos, column_names))
del(column_names)
column_pos

cols = [5, 9, 10, 22, 23, 24, 38, 39, 40, 41]

jsons_df.drop(columns = jsons_df.columns[cols],axis=1,inplace=True)

jsons_df

filename_2 = str(input('Enter a CSV filename to save (must end in .csv)'))

jsons_df.to_csv(filename_2) 

call = 'gsutil cp /home/lucapalmer98/project/csvs/' + filename_2 + ' gs://ust_bucket'

call

subprocess.call([call], shell =  True)
