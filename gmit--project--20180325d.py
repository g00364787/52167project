# -*- coding: utf-8 -*-
#
# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-03-25
# PROJECT
# A script to...
# Analyse the IRIS.CSV file known as FISCHER's IRIS data file.
# 
# all own work and with help from references
#
# references used:
# https://docs.python.org/2/library/csv.html
# accessed: 2-mar-2018
#
# https://pythonprogramming.net/reading-csv-files-python-3/
# accessed: 2 mar 2018
# 
# https://stackoverflow.com/questions/8234445/python-format-output-string-right-alignment
# accessed: 2 mar 2018
#
# http://www.tutorialspoint.com/python/string_rjust.htm
# accessed: 2 mar 2018
#
# http://www.tutorialspoint.com/python/string_rjust.htm
# accessed: 2 mar 2018
#
# import the library that can deal with CSV type data
import csv
#
# import the library that provides graphical output
import matplotlib.pyplot as plt
#
# import the library that has the specialised functions for number handling
import numpy as np
#
#
#
# setup the required data for the progam to run
filename = "iris.csv"
delim = ","
index = 0
idx = 0
l = 0
c = ""
line_in = ""
field = []
line_count1 = 0
line_count2 = 0

# create lists (arrays) for the values of each aspect of the iris.csv file
SepalLengthCm = np.array([],dtype=float)
SepalWidthCm = np.array([],dtype=float)
PetalLengthCm = np.array([],dtype=float)
PetalWidthCm = np.array([],dtype=float)
Species = np.array([])
line_in = "++"

SLmean = 0.01
SWmean = 0.01

SepLmean = -0.01
SepWmean = -0.01
PetLmean = -0.01
PetWmean = -0.01

print("# Program is running...")
print("# Opening: ",filename)
with open(filename) as f:
    while( len(line_in)>1):
        line_in = f.readline().strip()
        line_count1 = line_count1+1
        if ( len(line_in)>0 ):            
            field=[]
            for w in line_in.split(","):
                field.append(w)

            s0 = field[0]
            if ( ord(s0[0]) <64 ):
                line_count2 = line_count2+1                
                f0 = float(   (field[0]))
                f1 = float(   (field[1]))
                f2 = float(   (field[2]))
                f3 = float(   (field[3]))
                print (f0)
                print (f1)
                print (f2)
                print (f3)
                np.append(SepalLengthCm,f0)
                np.append(SepalWidthCm ,f1)
                np.append(PetalLengthCm,f2)
                np.append(PetalWidthCm ,f3)                
                print (SepalLengthCm)
f.close()
print("# End of file")
print("Line count: "+str(line_count1)+" "+str(line_count2))

SepLmean = np.mean(SepalLengthCm)
SepWmean = np.mean(SepalWidthCm)
PetLmean = np.mean(PetalLengthCm)
PetWmean = np.mean(PetalWidthCm)

print(SepLmean)
print(SepWmean)
print(PetLmean)
print(PetWmean)

print("# Program is finished.")