# -*- coding: utf-8 -*-
#
# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-04-22
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
sampleORpopulation = 'p'


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

def boxplot(ary1 = [],namOfArr = ""):
    plt.boxplot(ary1)
    plt.figtext(0.80, 0.08, arytitle,
            backgroundcolor='white', color='black', weight='roman')            
    plt.show()  
    return 0

    
def stddev(ary = [],sampORpop = ''):
    sigma = 0
    xbar = float(avg(ary))
    if ( sampORpop == 'p' ):
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
    return( round(max(ary)-min(ary),roundoff)  )
    
def numberof(ary = []):
    return (len(ary))

def total(ary = []):
    return (round(math.fsum(ary),roundoff))
            
def avg(ary = []):
    xbar = -0.01    
    xbar = math.fsum(ary) / len(ary)    
    return( round( xbar,roundoff))

def meedian(ary = []):
    return (statistics.median(ary) )

def statsof(ary = [], namOfArr = "", filnam = "",sampORpop = ''):
    print(namOfArr)
    print(dashes[0:len(namOfArr)])
    print("Samples  : "+ str(numberof(ary)))
    print("Maximum  : "+ str(max(ary)))
    print("Minimum  : "+ str(min(ary)))
    print("Range    : "+ str(maxtomin(ary)))
    print("Average  : "+ str(avg(ary)))
    print("Median   : "+ str(meedian(ary))
    print("Std Dev  : "+ str(stddev(ary,sampORpop)))
    if (len(filnam)>0 ):
        f = open(filnam,"a")
        f.write(namOfArr+"\n")   
        f.write(dashes[0:len(namOfArr)]+"\n")
        f.write("Samples  : "+ str(numberof(ary))+"\n")  
        f.write("Maximum  : "+ str(max(ary))+"\n")
        f.write("Minimum  : "+ str(min(ary))+"\n")
        f.write("Range    : "+ str(maxtomin(ary))+"\n")
        f.write("Average  : "+ str(avg(ary))+"\n")
        f.write("Median   : "+ str(meedian(ary))+"\n")
        f.write("Std Dev  : "+ str(stddev(ary,sampORpop))+"\n")
        f.write("\n")
        f.close()
#        print("# (Output sent to :'"+filnam+"' also.)")
    print("")
    return 0

def cleanreportfile():
    f = open(output_filename,"w")
    f.close()
    return 0


#
# MAIN PROGRAM
#
print("# Program is running...")

print("# Cleaning any previous report fle.")
cleanreportfile()

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

            # using the first field, test if its numeric or not
            s0 = field[0]
            # only accept lines that begin with a numeric
            # this will filter out lines that could cause errors
            if ( ord(s0[0]) > 47 and ord(s0[0]) < 64 ):
                # increment the used line counter
                line_count2 = line_count2+1      
                # convert the strings into float numbers
                f0 = float(field[0])
                f1 = float(field[1])
                f2 = float(field[2])
                f3 = float(field[3])
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
print("# Line count: "+str(line_count1)+" "+str(line_count2))

# announce the stats of each array
x = statsof(SepalWidthCm,"Sepal Width (cm)",output_filename,sampleORpopulation)
x = statsof(SepalLengthCm,"Sepal Length (cm)",output_filename,sampleORpopulation)
x = statsof(PetalWidthCm,"Petal Width (cm)",output_filename,sampleORpopulation)
x = statsof(PetalLengthCm,"Petal Length (cm)",output_filename,sampleORpopulation)


x = boxplot(SepalWidthCm,"Sepal Width CM")

# announce end of program to the user
print("# Program is finished.")
      
      
      
      
      