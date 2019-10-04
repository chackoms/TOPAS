# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import csv as csv
import numpy as np
import matplotlib.pyplot as plt


csv_file_object=csv.reader(open('/home/michael/Documents/Topas_Work/PhaseSpaceAtTinExit.csv',newline=''),delimiter=' ')

data=[]

for row in csv_file_object:
    hu=",".join(string for string in row if len(string) > 0)
    ho=hu.split(',')
    data.append(ho)

data=np.array(data)

test=np.array([])
test=np.empty([1,10])
for x in range(0,data.shape[0]):
    testy=np.array(data[x],np.float64)
    test=np.vstack([test,testy])
    
test=test[1:len(test)+1]    
    
test=test[np.where(test[:,5]>0.1199)]

print(test.shape[0]/100000)




"plt.figure()"
"plt.hist(test,bins='auto')"