# -*- coding: utf-8 -*-
#
# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-04-27
# Written using:  SPYDER v3.2.4  part of Anaconda package.
#
# PROJECT
# A script to...
# Analyse the IRIS.CSV file known as FISCHER's IRIS data file.
# 
# all own work and with help from references 
# - see supporting files for references visited and/or used
#
# import the library that provides graphical output
import matplotlib.pyplot as plt
#
#
# import the math library to calculate 
# square root, more accurate summing of floating point numbers and power_of
import math
#
# import functionality for computing some statistics
import statistics
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
#tempf1 = 0.1
#tempf2 = 0.1


# A routine to generate a single box plot to the screen
# the input arry is in  ary1 and the name of the arry is in namOfArr
def boxplot(ary1 = [],namOfArr = ""):
    plt.boxplot(ary1)
    plt.figtext(.40, .92, namOfArr,backgroundcolor='white', color='black', weight='roman')            
    print("Box plot of "+namOfArr)
    plt.ylabel('CM')
    plt.xlabel(' ') 
    plt.show()  
    print("#")
    return( 0)
    
# a routine to generate a multiple 4 column box plot
# the arrays are in  ary1,ary2,ary3,ary4
# the names of the arrays are in namfArr1,namfArr2,namfArr3,namfArr4
def manyboxplot(ary1 = [], namOfArr1 = "", ary2 = [], namOfArr2 = "", 
                ary3 = [], namOfArr3 = "", ary4 = [], namOfArr4 = ""):
    print("Multiple Box plot")
    tmpary = []
    tmpary.append(ary1)
    tmpary.append(ary2)
    tmpary.append(ary3)
    tmpary.append(ary4)     
    plt.xlabel(namOfArr1+" | "+namOfArr2 + " | "+namOfArr3 + " | "+namOfArr4)
    plt.ylabel('CM')
    #plt.figtext(.40, .92, namOfArr,backgroundcolor='white', color='black', weight='roman')            
    #print("Box plot of "+namOfArr)
    plt.boxplot(tmpary)
    plt.show()  
    print("#")
    return(0)
    
# a routine to generate scatter plot
# the array to plot is in ary1
# the name of the arry is in namOfArr
# for the X-axis index to match the contents of the input array, a temp arry
# called  tmpx is made to be the same length as the input array 'ary1'    
def scatplot(ary1 = [], namOfArr = ""):
    print("#")
    print ("# Scatter plot of "+ namOfArr +" data.")
    tmpx = []
    # generate numbers for the X axis that is the same size as the incoming array
    for x in range(len(ary1)):
        tmpx.append(float(x+1))
        
    plt.scatter(tmpx,ary1)        
    plt.xlabel('Index')
    plt.ylabel('CM')
    plt.show()
    return(0)

# routine to generate a normal-probability curve
# inputs are input arry and name of array
# calculates internal array of step values between each array X-value
# Generates Scatter plot where normal data will appear S-shaped
def norm_prob(ary1 = [], namOfArr = ''):
    print ("#")
    print ("# Normal Probability Plot of "+namOfArr+" data.")
    ary1.sort()
    tmpx = []
    maxx = len(ary1)+1
    # calculate the stepped values from 0.000 to 99.99999 over the number of samples
    for x in range(len(ary1)):
        tmpx.append(float(x/maxx)*100)
        
    plt.scatter(ary1,tmpx)        
    plt.xlabel('CM')
    plt.ylabel('%')
    plt.show()
    print("#")
    return(0)

# routine to calculate the standard deviation of a supplied array
# an extra input is to decide if the input array is a sample or the populatiion    
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
      
# a routine to calculate the range of  MIN --- MAX    
def maxtomin(ary = []):
    return( round(max(ary)-min(ary),roundoff)  )
    
# a routine to return the length of the supplied array    
def numberof(ary = []):
    return (len(ary))

# a routine to calculate the total of the supplied array
def total(ary = []):
    return (round(math.fsum(ary),roundoff))

# a routine to calculate the average of the supplie input array            
def avg(ary = []):
    xbar = -0.01    
    xbar = math.fsum(ary) / len(ary)    
    return( round( xbar,roundoff))

# a routine to calculate the media of a supplied array
# avoiding the use of the term  media for the routine as this is a keyword.
def mdian(ary = []):
    return (statistics.median(ary) )

# a routine to display the statistics of a supplied array
def statsof(ary = [], namOfArr = "", filnam = "",sampORpop = ''):
    tempf1 = 0.1
    tempf2 = 0.1
    tempsr = 0.1
    strgsr = ""
    print("#")
    print(namOfArr)
    print(dashes[0:len(namOfArr)])
    print("Samples . . : "+ str(numberof(ary)))
    print("Maximum . . : "+ str(max(ary)))
    print("Minimum . . : "+ str(min(ary)))
    print("Range   . . : "+ str(maxtomin(ary)))	
    print("Average . . : "+ str(avg(ary)))
    print("Std Dev . . : "+ str(tempsr) )
    tempf1 = stddev(ary,sampORpop)
    tempf2 = maxtomin(ary)
    tempsr = int(1000*(tempf2 / tempf1))/1000
    strgsr = str(tempsr).rjust(5," ")
    print("Range:Stddev: "+strgsr+":1")
    if (len(filnam)>0 ):
        f = open(filnam,"a")   
        f.write(namOfArr+"\n")   
        f.write(dashes[0:len(namOfArr)]+"\n")
        f.write("Samples . . : "+ str(numberof(ary))+"\n")  
        f.write("Maximum . . : "+ str(max(ary))+"\n")
        f.write("Minimum . . : "+ str(min(ary))+"\n")
        f.write("Range   . . : "+ str(maxtomin(ary))+"\n")
        f.write("Average . . : "+ str(avg(ary))+"\n")
        f.write("Std Dev . . : "+ str(stddev(ary,sampORpop))+"\n")
        f.write("Range:Stddev: "+strgsr+":1")
        f.close()
#        print("# (Output sent to :'"+filnam+"' also.)")
    return 0

# a routine to create an empty file or to overwrite an existing file 
# so that the latest output is all that is in the report file.
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
x = statsof(SepalLengthCm,"Sepal Length (cm)",output_filename,sampleORpopulation)
x = statsof(SepalWidthCm,"Sepal Width (cm)",output_filename,sampleORpopulation)
x = statsof(PetalLengthCm,"Petal Length (cm)",output_filename,sampleORpopulation)
x = statsof(PetalWidthCm,"Petal Width (cm)",output_filename,sampleORpopulation)

# Generate some box plots for the data
print("# Box Plots")
x = boxplot(SepalLengthCm,"Sepal Length CM")
x = boxplot(SepalWidthCm,"Sepal Width CM")
x = boxplot(PetalLengthCm,"Petal length CM")
x = boxplot(PetalWidthCm,"Petal Width CM")

# Add in a comparison multiple boxplot
print("# Multiple box plot")
x = manyboxplot(SepalLengthCm, "Sepal length CM", SepalWidthCm, "Sepal Width CM",
                PetalLengthCm, "Petal Length CM", PetalWidthCm, "Petal Width CM")

# generate some Scatter plots.  These might give some indicate of clustering.
print("# Scatter Plots")
x = scatplot(SepalLengthCm, "Sepal Length CM")
x = scatplot(SepalWidthCm, "Sepal Width CM")
x = scatplot(PetalLengthCm, "Petal Length CM")
x = scatplot(PetalWidthCm, "Petal Width CM")

# generate some normal-probability graphs.
# if these produce a S-shape type graph then the data could be considered NORMAL
# as the S-shape is really a Bell Curve where o half is twisted around.
print("# Normal Probability Plots")
x = norm_prob(SepalLengthCm, "Sepal Length CM")
x = norm_prob(SepalWidthCm, "Sepal Width CM")
x = norm_prob(PetalLengthCm, "Petal Length CM")
x = norm_prob(PetalWidthCm, "Petal Width CM")

# announce end of program to the user
print("# Program is finished.")
     