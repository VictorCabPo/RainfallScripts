#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Victor Caballero
Edenvale Young
02/10/2017
"""
import os, pandas, numpy, glob

Folder = input("Folder with CSV: ")

os.chdir(Folder)

ListTime = ['9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00',
            '18:00','19:00','20:00','21:00','22:00','23:00','24:00','1:00','2:00','3:00','4:00',
            '5:00','6:00','7:00','8:00']

YetP =[0.002,0.010,0.035,0.008,0.006,0.015,0.003,0.003,0.007,
       0.014,0.016,0.031,0.027,0.050,0.089,0.328,0.128,0.072,0.032,
       0.067,0.037,0.014,0.001,0.003]

myYet = "/Yetogramas"

slash = "/"

pathMyYet = Folder + myYet

if not os.path.isdir(pathMyYet):
    os.makedirs(pathMyYet)
    print("The New Folder Yetogramas Was Created")

CSVFolder = glob.glob("*.csv")

for Fcsv in CSVFolder:
    
    nameCSV = os.path.basename(Fcsv)
    
    print("******************** " + nameCSV)
    
# we open the csv and skip the first rows

    df = pandas.read_csv(Fcsv, skiprows = [0,1,2,3,4,5])
    
    print(df.shape)
    #print(df)

# As there are some NaN in the dataframe, we have to remove them

    #df2 = df[df.Date.str.contains('NaN') == False]
    #df2 = df['Date'].fillna(False)        
    #df3 = df2['Value'].fillna(0.0, inplace = True)
    df2 = df[df.Date.str.contains('NaN') == False]        
           
  
    #df2['Value'].fillna(0.0, inplace = True)
    
                  
# As there are some values negatives, we have to remove them and to give them the value of zero
# we convert it to a list in order to change the negatives values easily.

    #l=df2['Value'].tolist()
    
    df3 = df2[df2.Value >= 0.0]

# we change the negative values by zero.  To do so, we create a new list to store the new data without NaN

    #l2 = []

    #for n in l:
    #    if isinstance(n, str):
    #       del l[n]
    #    elif n < 0.0:
    #       l.remove(n)
    #    else:
    #       l2.append(n)
           
# another way to detect strings is import types, if type(a) is types.str:  
           
    print("The File " + nameCSV + " Has Neither Negatives nor NaN")

# we multiply the list with the 24h rainfall by the factors of the hyetograph
    
    l2 = df3['Value'].tolist()

    li=[]

    for el in l2:
        n=[i*el for i in YetP]
        li.append(n)      
    
    dfAr = pandas.DataFrame(numpy.array(li))

    dfArS = dfAr.stack().reset_index(drop=True)
    
    rows = len(dfAr)  
    
# we are going to get the column with the date
# we create a list with the column Date from df

    dl = df3["Date"].tolist()

# we multiply the elements of the list by 24.  To do o, it is converted to an aray

    dl2 = numpy.repeat(dl,24)

# we convert the array to a list with the proper dates

    dl2P = dl2.tolist() # list for csv

# we repeat the operation of the date wth the time steps
# we multiply the list by 37226 (37226*24=893424 rows)

    Lit = ListTime*rows # list for the csv

# we create a dictionary with the lists of the future csv

    csvD = {"Date": dl2P, "Time": Lit, "mm": dfArS }

    csvDF = pandas.DataFrame(csvD)
    
    #nameCSV = os.path.basename(Fcsv)
    
    fileRe = pathMyYet + slash + nameCSV

    csvDF.to_csv(fileRe, index = None)
    
    print(len(csvDF))
    print("-------------------- Done")

print("Finished")

