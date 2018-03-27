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
SepalLengthCm = []
SepalWidthCm = []
PetalLengthCm = []                            
PetalWidthCm = []                            
Species = []                            
line_in = "++"

SLmean = 0.01
SWmean = 0.01

SepL_mean = -0.01
SepW_mean = -0.01
PetL_mean = -0.01
PetW_mean = -0.01

SepL_max = -0.01
SepW_max = -0.01
PetL_max = -0.01
PetW_max = -0.01

SepL_min = 32766
SepW_min = 32766
PetL_min = 32766
PetW_min = 32766

SepLtotal = 0
SepWtotal = 0
PetLtotal = 0
PetWtotal = 0

def maxtomin(ary = []):
    return(max(ary)-min(ary)
    
def numberof(ary = []):
    return (len(ary))

def total(ary = []):
    return (sum(ary))
            
def aver(ary = []):
    avg = -0.01    
    avg = sum(ary) / len(ary)    
    return avg


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
                SepalLengthCm.append(f0)
                SepalWidthCm.append(f1)
                PetalLengthCm.append(f2)
                PetalWidthCm.append(f3)
#                print (f0)
#                print (f1)
#                print (f2)
#                print (f3)
f.close()
print("# End of file")
print("Line count: "+str(line_count1)+" "+str(line_count2))
print(max(SepalWidthCm),min(SepalWidthCm),(int(max(SepalWidthCm)-min(SepalWidthCm))*1000)/1000)
print(max(SepalLengthCm),min(SepalLengthCm),(int(max(SepalLengthCm)-min(SepalLengthCm))*1000)/1000)
print(max(PetalWidthCm),min(PetalWidthCm),max(PetalWidthCm)-min(PetalWidthCm))
print(max(PetalLengthCm),min(PetalLengthCm),max(PetalLengthCm)-min(PetalLengthCm))

SepW_mean = aver(SepalWidthCm)
print(sum(PetalLengthCm), len(PetalLengthCm),sum(PetalLengthCm)/ len(PetalLengthCm) )
print(SepW_mean)
print("# Program is finished.")
      


### storage area down here
#               SepLtotal = SepLtotal + f0
#               SepWtotal = SepWtotal + f1
#               PetLtotal = PetLtotal + f2
#               PetWtotal = PetWtotal + f3
#               if ( f0 > SepWmax): SepWmax = f0
#               if ( f1 > SepLmax): SepLmax = f1
#               if ( f2 > PetWmax): PetWmax = f2
#               if ( f3 > PetLmax): PetLmax = f3
#               
#               if ( f0 < SepWmin): SepWmin = f0
#               if ( f1 < SepLmin): SepLmin = f1
#               if ( f2 < PetWmin): PetWmin = f2
#               if ( f3 < PetLmin): PetLmin = f3
