# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:52:22 2022

@author: jh
"""

import pandas as pd
import csv
import sys
from webbrowser import Konqueror
from pandas import DataFrame, Series
import re

poem=pd.read_csv('윤동주.csv', encoding='utf-8')
poem = poem.loc[:,'시']

myfile = open("윤동주.txt",
              mode = 'w',
              encoding = 'UTF-8',
              newline = None,
              buffering=-1,
              errors = None,
              closefd = True,
              opener=None)

poem_string = ''

for i in range(0,len(poem)) :
    poem[i] = poem[i].replace("\n ", '\n')
    poem[i] = poem[i].replace('\n\n' , '<yun>')  
    myfile.write('"<s>' + poem[i] + '</s>"' + '\n')

myfile.write(poem_string)
myfile.close()