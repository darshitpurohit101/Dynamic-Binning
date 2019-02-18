#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:15:43 2019

@author: darshit
"""
import csv
import statistics

var = []	
myfile = open('practical4sampledata.csv') 
with myfile:
	reader = csv.DictReader(myfile)
	for row in reader:
		var.append(int(row['Marks']))

maxVal = max(var)
minVal = min(var)
newMax = 1
newMin = 0
zscore = 0
ds = 0
x = '1'
normminmax = []
normz = []
dsnorm = []
mean = statistics.mean(var)
std = statistics.stdev(var)



for i in range(len(var)):
        minmax = (((var[i] - minVal)/(maxVal-minVal))*(newMax - newMin))+newMin
        normminmax.append(minmax)
        zscore = ((var[i]-mean)/std)
        normz.append(zscore)
        for j in range(len(chr(var[i]))):
            x = x + '0'
        ds =  (var[i]/int(x))
        dsnorm.append(ds)
        x = '1'
 
print("Marks= ",var)        
print("MinMax= ",normminmax)
print("Z-Score= ",normz)
print("Decimal-Scaling= ",dsnorm)
    