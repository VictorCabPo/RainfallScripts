#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Victor Caballero
Edenvale Young
03/10/2017
"""
import os, random, pandas, glob
import seaborn as sns

Path = input("Folder: ")

os.chdir(Path)

file = random.choice(os.listdir(Path))

print("****************************************************")

print("File Randomly Selected: " + file)

dfC = pandas.read_csv(file)

lo = len(dfC)

Id = random.randint(0, len(dfC))

print("Id Selected in the CSV: " + str(Id))

Date = dfC.loc[Id][0]

print("The Date Randomly Selected was: " + str(Date))

SumM = dfC['mm'][dfC['Date'] == Date].sum()

print("Total Precipitation for this Date: " + str(SumM))

Hist = dfC[dfC['Date'] == Date]

HistDF = pandas.DataFrame(Hist)


#################################################################

NameFol = os.path.basename(str(Path)) 

#BackPath = "../" + NameFol

os.chdir("..")

OrigFile = glob.glob(file)

NewPath = os.getcwd()

slash = '/'

Pcsv = NewPath

Ncsv = Pcsv + slash + file


dfOrig = pandas.read_csv(Ncsv, skiprows = [0,1,2,3,4,5])

Row = dfOrig[dfOrig['Date'] == Date]

print("****************************************************")
print("The Original Data in the Original CSV were: ")
print(Row)
print("****************************************************")

#################################################################

sns.set(style="darkgrid")

BarHis = HistDF.plot.bar(x='Time', y='mm', color = 'darkblue')

#BarHis.savefig("Hyeto_" + str(Date) + ".png")

print(BarHis)


