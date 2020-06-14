# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:35:02 2020

@author: welkin
"""

from py2neo import Graph,Node,Relationship
import numpy as np
import pandas as pd
io='nodes.csv'
names=['nam','i']
df=pd.read_csv(io,usecols=[0,1],names=names,index_col='i')
print(df)
# id_list=[]
# name_list=[]

# for data in df:
#     id_l,name_l=df[data]
#     id_list.append(id_l)
#     name_list.append(name_l)
    