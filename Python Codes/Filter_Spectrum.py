#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:16:44 2019

@author: michaelchacko
"""

import csv as csv
import numpy as np
import matplotlib.pyplot as plt


csv_file_object=csv.reader(open('/home/michael/Documents/Topas_Work/E_Spectrum_Values.csv',newline=''),delimiter=' ')
csv_file_object1=csv.reader(open('/home/michael/Documents/Topas_Work/E_Spectrum_Weights.csv',newline=''),delimiter=' ')

values=[]
weights=[]

for row in csv_file_object:
    values.append(row)

for row in csv_file_object1:
    weights.append(row)

values=[x for x in values if x]
weights=[x for x in weights if x]

weights=np.array(weights)
values=np.array(values)
values[0]='0.01'
weights[0]='0'


v=np.empty([values.shape[0],1])
w=np.empty([weights.shape[0],1])
for x in range(0,values.shape[0]):
    v[x]=float(values[x])

for x in range(0,weights.shape[0]):
    w[x]=float(weights[x])

weighted_average=(v*w)
print(sum(weighted_average))

org_hist=plt.hist(v,bins=np.arange(v[0],v[-1],0.1),range=None,density=None,weights=w,color='blue')
plt.ylabel('Weight (Scaled to 1)')
plt.xlabel('Energy (keV)')


    
Output = [sum(v[i:i + 3])/3 
          for i in range(len(v) - 3 + 1)] 

vo=np.empty([len(v)-3+1,1])

for i in range (len(v)-3+1):
    vo[i]=sum(v[i:i + 3])/3 

vo=vo[1::3]

