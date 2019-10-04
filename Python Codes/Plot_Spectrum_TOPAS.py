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
    
energies=test[:,5]
energies=energies*1000
print(np.average(energies))

org_hist=plt.hist(energies,bins=np.arange(min(energies),max(energies),1),range=None,density=None,color='red')
plt.ylabel('Counts')
plt.xlabel('Energy (keV)')            
plt.title('Spectrum at Tin Exit')  