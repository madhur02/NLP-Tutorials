# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:56:07 2019

@author: J554696
"""

import pandas as pd
import numpy as np
df = pd.read_excel(r"C:\Users\J554696\Desktop\A1 Sector .xlsx", names= 'A B C D E F G H I J K L'.split())

df.dropna(thresh=1 , inplace = True)
df.dropna(thresh=1 ,axis=1, inplace = True)
df.reset_index(inplace=True)

'''
df.drop(['index','A'], axis = 1, inplace = True)
df.rename(columns={'B':"PERF Cusip or Sedol PERF SECTOR",
                          'D':'OMS Average Weight',
                           'E': "OMS Total Return",
                           'F': "S&P Total Weight",
                           'G': "S&P Total Return",
                          'H':'Variation Total Weight',
                          'I':'Variation Total Return',
                           'J':"Attribution Analysis Allocation Effect",
                           'K': "Allocation Analysis Selection + Interaction",
                           'L': "Allocation Analysis Total Effect"
                            }, 
                 inplace=True)
df.drop([0,1,2], axis = 0 , inplace = True)
for i in df.columns[1:]:
    df[i] = df[i].astype(float)

'''