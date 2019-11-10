#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON data generator
==============
Generates some random data and writes it down to JSON 
format into the buffer file
Created on Sun Nov  3 12:04:51 2019

@author: luisarribas
"""

import uuid
import json
import random
import config_file as cf

n_objects = 200


def run():
    clear_buffer()
    json_str = '{'
    for i in range(n_objects):
        key = uuid.uuid1()
        val1 = random.randint(1, 1000)
        val2 = random.gauss(0, 1)
        key_val_dict = '{' + ' "key":"{}","val 1":{},"val 2":{}'.format(key, val1, val2) + '}'
        json_str = json_str + key_val_dict
        if i < n_objects - 1:
            json_str = json_str + ',' + '\n'
    json_str = json_str + '}'
    with open('buffer.txt', 'w') as json_file:
        json.dump(json_str, json_file)


def clear_buffer():
    buffer = cf.configuration.get('buffer')
    file_object = open(buffer, 'w')
    file_object.writelines('')
    file_object.close()


if __name__ == '__main__':
    run()
