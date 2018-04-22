# -*- coding: utf-8 -*-
#
# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-03-27
# PROJECT
# A script to...
# Analyse the IRIS.CSV file known as FISCHER's IRIS data file.
# 
# all own work and with help from references 
# - see supporting file all references visited and/or used
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

# to be able to set the roundoff decimal places easily
roundoff = 5

# to be able to edit the output filename easily
output_filename = "IRIS_report.txt"

# to control the calculation ostandard deviation
# sample uses   n-1   population uses  n
sample_r_population = 's'


dashes = "==============================="
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

def stddev(ary = [],popsam = ''):
    sigma = 0
    xbar = float(avg(ary))
    if ( popsam == 'p' ):
        n = numberof(ary)    
    else:
        n = numberof(ary) -1
        
    i = 0
    while (i<n):        
        sigma = sigma + math.pow( (float(ary[i]) - xbar)  ,2)
        i=i+1
    sigma = sigma / (n)
    sigma = math.sqrt(sigma)
    return(round(sigma,roundoff))
      
def maxtomin(ary = []):
    return( round(     max(ary)-min(ary),roundoff)  )
    
def numberof(ary = []):
    return (len(ary))

def total(ary = []):
    return (round(math.fsum(ary),roundoff))
            
def avg(ary = []):
    xbar = -0.01    
    xbar = math.fsum(ary) / len(ary)    
    return( round( xbar,roundoff))

def statsof(ary = [], namOfArr = "", filnam = ""):
    print(namOfArr)
    print(dashes[0:len(namOfArr)])
    print("Maximum  : "+ str(max(ary)))
    print("Minimum  : "+ str(min(ary)))
    print("Average  : "+ str(avg(ary)))
    print("Range    : "+ str(maxtomin(ary)))
    print("Samples  : "+ str(numberof(ary)))
    print("Std Dev  : "+ str(stddev(ary,sample_r_population)))
    if (len(filnam)>0 ):
        f = open(filnam,"a")
        f.write(namOfArr+"\n")   
        f.write(dashes[0:len(namOfArr)]+"\n")
        f.write("Maximum  : "+ str(max(ary))+"\n")
        f.write("Minimum  : "+ str(min(ary))+"\n")
        f.write("Average  : "+ str(avg(ary))+"\n")
        f.write("Range    : "+ str(maxtomin(ary))+"\n")
        f.write("Samples  : "+ str(numberof(ary))+"\n")
        f.write("Std Dev  : "+ str(stddev(ary,sample_r_population))+"\n")
        f.write("\n")
        f.close()
        print("(Output sent to :'"+filnam+"' also.)")
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
            # only accept lines that begin with a numeric
            # this will filter out lines that could cause errors
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
x = statsof(SepalWidthCm,"Sepal Width",output_filename)
x = statsof(SepalLengthCm,"Sepal Length",output_filename)
x = statsof(PetalWidthCm,"Petal Width",output_filename)
x = statsof(PetalLengthCm,"Petal Length",output_filename)


# announce end of program to the user
print("# Program is finished.")
      
      
      
      
      