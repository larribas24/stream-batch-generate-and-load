#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stream data generator
==============
Generates some random CSV data and writes it into the buffer file
every n seconds. When called buffer is cleared
Created on Sun Nov  3 12:04:51 2019

@author: luisarribas
"""

import time
import uuid
from random import choice
import config_file as cf


def run():
    clear_buffer()

    while (True):
        time.sleep(1)
        # generates a random int [1-10] and writes a string
        # just for testing purpose
        numbers = list(range(10))
        key = uuid.uuid1()
        val1 = str(choice(numbers))
        val2 = str(choice(numbers))
        str1 = '{},{},{}\n'
        str1 = str1.format(key, val1, val2)

        # reads input file
        buffer = cf.configuration.get('buffer')
        file_object = open(buffer, 'a')

        # write input string on input file
        file_object.writelines(str1)

        # close file
        file_object.close()


def clear_buffer():
    buffer = cf.configuration.get('buffer')
    file_object = open(buffer, 'w')
    file_object.writelines('')
    file_object.close()


if __name__ == '__main__':
    run()
