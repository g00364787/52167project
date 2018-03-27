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
# import the math library to calculate 
# square root, more accurate summing of floating point numbers and power_of
import math
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


def stddev(ary = []):
# assumption: input array will always be a sample - therefore will use   n-1    
    sigma = 0
    diff = -0.01
    xbar = aver(ary)
    n = numberof(ary)    
    i = 0
    while (i<n):        
        sigma = sigma + math.pow( (float(ary[i]) - float(xbar))  ,2)
        i=i+1
    sigma = sigma / ( n-1)
    sigma = math.sqrt(sigma)
    return(sigma)
      
def maxtomin(ary = []):
    return(max(ary)-min(ary)) 
    
def numberof(ary = []):
    return (len(ary))

def total(ary = []):
    return (math.fsum(ary))
            
def avg(ary = []):
    xbar = -0.01    
    xbar = math.fsum(ary) / len(ary)    
    return xbar

def statsof(ary = [], namOfArr = ""):
    print(namOfArr)
    print("=====================")
    print("Maximum  : "+ str(max(ary)))
    print("Minimum  : "+ str(min(ary)))
    print("Average  : "+ str(avg(ary)))
    print("Range    : "+ str(maxtomin(ary)))
    print("Count    : "+ str(numberof(ary)))
    print("Std Dev  : "+ str(stddev(ary)))
    print("")
    return 0
    

print("# Program is running...")
print("# Opening: ",filename)
with open(filename) as f:
    while( len(line_in)>1):
        # retrieve one line of the file and strip and whitespace off the line
        line_in = f.readline().strip()
        # increment the line in counter
        line_count1 = line_count1+1
        # only if the line is useable ...
        if ( len(line_in)>0 ):        
            # split the input line up into data fields
            field=[]
            for w in line_in.split(","):
                field.append(w)

            # using the firts field, test if its numeric or not
            s0 = field[0]
            # only accept lines that are numeric
            if ( ord(s0[0]) > 47 and ord(s0[0]) < 64 ):
                # increment the used line counter
                line_count2 = line_count2+1      
                # covert the strings into float numbers
                f0 = float(   (field[0]))
                f1 = float(   (field[1]))
                f2 = float(   (field[2]))
                f3 = float(   (field[3]))
                # add these converted numbers onto the array of float numbers
                SepalLengthCm.append(f0)
                SepalWidthCm.append(f1)
                PetalLengthCm.append(f2)
                PetalWidthCm.append(f3)
# close the file 
f.close()
# announce to the screen that the file is closed
print("# End of file")
# inform the user of how many lines used
print("Line count: "+str(line_count1)+" "+str(line_count2))

# announce the stats of each array
x = statsof(SepalWidthCm,"Sepal Width")
x = statsof(SepalLengthCm,"Sepal Length")
x = statsof(PetalWidthCm,"Petal Width")
x = statsof(PetalLengthCm,"Petal Length")


# announce end of program to the user
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
