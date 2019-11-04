#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON data reader
===========

reads JSON data writen on buffer file and prints it in a pandas dataFrame . 
Clears the buffer afterwards

Created on Sun Nov  3 12:38:37 2019

@author: luisarribas
"""

import json
import config_file as cf
import pandas as pd

buffer = cf.configuration.get('buffer')

def run():
    print('reading buffer...')
    with open(buffer, encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
    json_data = json_data[1 : len(json_data)]
    lines = json_data.split("\n")
        
    #remove comas
    lines = list(map(lambda s: s[:-1], lines))
       
    #get columns names and build empty dataframe
    lineDict = json.loads(lines[0])
    df = pd.DataFrame(columns = lineDict.keys() ) 
    
    for line in lines:
        #print(line)
        lineDict = json.loads(line)
        df = df.append(lineDict , ignore_index=True)
    df.set_index(keys = 'key', inplace = True) 
    
    print(df)           
    clear_buffer()
    
def clear_buffer():
    file_object = open(buffer,'w')
    file_object.writelines('')   
    file_object.close()  

if __name__ == "__main__":
    run()