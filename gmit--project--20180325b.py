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
SepalLengthCm = []
SepalWidthCm = []
PetalLengthCm = []
PetalWidthCm = []
Species = []
line_in = "++"

print("# Program is running...")
print("# Opening: ",filename)
with open(filename) as f:
    while( len(line_in)>1):
        line_in = f.readline().strip()
        line_count1 = line_count1+1
        s = len(line_in)
        if ( s>1 ):            
            line_count2 = line_count2+1
            idx=0
            field=[]
            for w in line_in.split(","):
                field.append(w)
                print("/"+w+"/")
            
            SepalLengthCm.append(float(field[0]))
            SepalWidthCm.append(float(field[1]))
            PetalLengthCm.append(float(field[2]))
            PetalWidthCm.append(float(field[3]))
            
#            print(" field0:"+field[0])
#            print(" field1:"+field[1])
#            print(" field2:"+field[2])
#            print(" field3:"+field[3])                
#            print(" field4:"+field[4])                
 
                           
print("# End of file")
print("Line count: "+str(line_count1)+" "+str(linecount2))
f.close()
print("# Program is finished.")