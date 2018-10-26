#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Victor Caballero
Edenvale Young
05/10/2017
"""
import os, pandas, glob

Folder = input("Folder with CSV: ")

print("For Kelani the format to choose the time period must be mm/dd/yyyy")

Start = input("Start Period: ")

End = input("End Period: ")

FData = input("Name of the folder? (e.g. May03): ")

os.chdir(Folder)

myYet = "/Yetogramas2"

slash = "/"

pathMyYet = Folder + myYet

if not os.path.isdir(pathMyYet):
    os.makedirs(pathMyYet)
    print("The New Folder Yetogramas2 Was Created")
    
if not os.path.isdir(pathMyYet + slash + FData):
    os.makedirs(pathMyYet + slash + FData)
    print("The New Folder " + FData + " Was Created")

CSVFolder = glob.glob("*.csv")

for csv in CSVFolder:
    print("----------------------------------------------------")
    print("Taken " + csv)
    print("----------------------------------------------------")
    csvDF = pandas.read_csv(csv) 
    DateList = csvDF['Date'].values.tolist()
    if not (Start or End) in DateList:
        print("The file " + csv + " does not have the period of time selected")
    else:
        print("----------------------------------------------------")
        print("The file " + csv + " has the period of time selected")
        print("----------------------------------------------------")
        try:
            ChopS = csvDF[csvDF['Date'] == Start]
            ChopE = csvDF[csvDF['Date'] == End]
            IdChopS = ChopS.index.values.tolist()[0]
            IdChopE = ChopE.index.values.tolist()[23]
            ListChop = list(range(IdChopS,IdChopE + 1))
            csvDFchop = csvDF.iloc[ListChop]
            Idcsv = csvDFchop.reindex(range(len(csvDFchop)))
            listID = Idcsv.index.values.tolist()
            csvDFchop['Hours'] = listID
            nameCSV = os.path.basename(csv)
            csvName = pathMyYet + slash + FData + slash + nameCSV
            csvDFchop.to_csv(csvName, index = None)
            Valmm = pandas.read_csv(csvName)
            if Valmm['mm'].sum() == 0:
                print('The csv ' + os.path.basename(csvName) + ' has no rainfall in this period of time')
                os.remove(csvName)
        except IndexError:
            pass
        continue
             
print("Done..... thanks!!!!")   
      
        
    
