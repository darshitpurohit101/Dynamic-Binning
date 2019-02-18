#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:24:23 2019

@author: darshit
"""
#BINNING

data = [1,7,12,17,3,20,24,11,35,48,56,27,33,44,60,70,99,33]
dataS = sorted(data) #Sorting data
x = int(input("Enter number of bins")) 
numofelem  = round(len(dataS)/x)
#print("numofelem",numofelem)
summ = 0
mean = 0
frm = 0
to = numofelem
lenofdata = len(dataS)

#print(dataS)

for i in range(x):
    
    if lenofdata > numofelem:
        
        for j in range(frm,to):
            summ = dataS[j] + summ
#            print(summ)
        mean = summ/numofelem
#        print("mean: ",mean)
        for x in range(frm,to):
            dataS[x] = mean
            
        summ = 0
        mean = 0
        frm = numofelem + frm
        to = numofelem + to
        lenofdata = lenofdata - numofelem
#        print("a",lenofdata)
#        print("b",numofelem)
        
    else:
        for j in range(frm,len(dataS)):
#             print("thisssss: ",dataS[j])
             summ = dataS[j] + summ
#             print("summmm: ",summ)
             mean = summ/numofelem
#             print("meannnn",mean)
             
        for x in range(frm,len(dataS)):
            dataS[x] = mean
#            print(dataS[x])
             
        summ = 0
        mean = 0
        
        
#    elif lenofdata < numofelem :         
#         print("data len",lenofdata)
#         
         
         
print(dataS)         