#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:43:21 2020

@author: michaelchacko
"""

import os
import glob
import numpy as np
import csv as csv
import matplotlib.pyplot as plt
from scipy.optimize import nnls


os.chdir('/Users/michaelchacko/Documents/Topas_Files/TOPAS/MLIC_simulation/BC_composition')
set=sorted(glob.glob('/Users/michaelchacko/Documents/Topas_Files/TOPAS/MLIC_simulation/BC_composition/*.csv'))

BP_library=np.empty([165,len(set)])

for x in range(0,len(set)):
    csv_file_object=csv.reader(open(set[x],newline=''),delimiter=',')
    data=[]
    count=0
    for row in csv_file_object:
        count+=1
        if count>8:
            hu=",".join(string for string in row if len(string) > 0)
            ho=hu.split(',')
            data.append(ho[-1])
            data_conv=np.array(data,np.float64)
            data_norm=data_conv/np.amax(data_conv)
        else:
            continue
    BP_library[:,x]=data_norm
    
#%% Make this a new function later. Auto opens phase space and extracts   
os.chdir('/Users/michaelchacko/Documents/Topas_Files/TOPAS/MLIC_simulation')
set=sorted(glob.glob('/Users/michaelchacko/Documents/Topas_Files/TOPAS/MLIC_simulation/*.csv'))
csv_file_object=csv.reader(open(set[1],newline=''),delimiter=',')
measured=[]
for row in csv_file_object:
    hu=",".join(string for string in row if len(string) > 0)
    ho=hu.split(',')
    measured.append(ho)

measured=np.array(measured)
measured=measured[8:]

test=np.array([])
test=np.empty([1,4])
for x in range(0,measured.shape[0]):
    testy=np.array(measured[x],np.float64)
    test=np.vstack([test,testy])
    
test=test[1:]

BP_measured=test[:,3]/np.amax(test[:,3]) 

#%% Curve fit using NNLS

coeff=nnls(BP_library,BP_measured)
coeff_x=coeff[0]
element_wise=np.multiply(coeff_x,BP_library)
dot_product=np.dot(BP_library,coeff_x)
final_weighted_element_wise=np.sum(element_wise,axis=1)
plt.figure(0)
plt.plot(np.arange(0,180),final_weighted_element_wise)
plt.figure(1)
plt.plot(np.arange(0,180),BP_measured)

#%% Find WET
