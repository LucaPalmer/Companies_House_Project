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
import time
import os
import sys

os.chdir('/home/lucapalmer98/project/jsons')

with requests.get('https://stream.companieshouse.gov.uk/companies', auth = ('',''), stream = True) as r:
    if r.status_code == 200:
        print("Connection OK! Gathering data...")
        filename = str(input('Enter a json filename to save (must end in .txt)'))
        filepath = '/home/lucapalmer98/project/jsons/' + filename
        print("Your filepath: " + filepath)
    with open(filepath, 'w') as g:
        count_check = 0
        limit = int(input("Enter a number of JSONs to gather: "))
        for line in r.iter_lines():
            if line:
                if count_check != limit:
                    decoded_line = line.decode('utf-8')
                    g.write(str(decoded_line))
                    g.write("\n")
                    count_check +=1
                    print("JSON Quantity: ", count_check, end="\r")
                elif count_check == limit:
                    sys.exit('JSON Limit Reached')
                #time.sleep(5)


