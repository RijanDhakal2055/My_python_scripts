#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:26:59 2021

@author: paul13
"""

import pandas as pd
in_data = pd.read_csv('chromatin_counts.txt',delim_whitespace = True)
in_data.columns = ['Orthogroup','species','count']
print(in_data.shape)
print(in_data.head())
new_data = pd.pivot_table(in_data,index = 'Orthogroup', columns = 'species', values = 'count')
new_data = new_data.reset_index()
print(new_data.head())

new_data.to_csv('Chromatincounts.tsv',index = False, sep = '\t')

