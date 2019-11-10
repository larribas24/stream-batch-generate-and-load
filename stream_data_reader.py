#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stream data reader
===========

reads data writen every n seconds on buffer file and prints it line by line. 
Clears the buffer afterwards

Created on Sun Nov  3 12:38:37 2019

@author: luisarribas
"""

import time
import config_file as cf

buffer = cf.configuration.get('buffer')


def run():
    while True:
        time.sleep(3)
        print('reading buffer...')

        file_object = open(buffer, "r")
        data = file_object.readlines()
        for line in data:
            key, value = format_line(line)
            print(f'UUID: {key} value 1: {value[0]} value 2: {value[1]}')
        clear_buffer()


def format_line(line):
    line = line.strip()  # strip out carriage return
    key_value = line.split(",")
    key = key_value[0]  # key is first item in list
    value = (key_value[1], key_value[1])  # value is 2nd item
    return key, value  # print a string, tab, and string


def clear_buffer():
    file_object = open(buffer, 'w')
    file_object.writelines('')
    file_object.close()


if __name__ == "__main__":
    run()
