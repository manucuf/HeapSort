#!/usr/bin/python
import sys
import os
import shutil

import CSVHelper
import PlotHelper

xaxis = 'Size' # None
yaxis = 'Time' # None
figuretitle = ['HeapSort Performance', 'HeapSort comparison with InsertionSort'] #None
unitofmeasure = 'Time (s)' # None
delimiter = ',' # None

csvfilesHeap = ['resBuildMaxHeap1.csv', 'resBuildMaxHeap2.csv', 'resBuildMaxHeap3.csv', 'resBuildMaxHeap4.csv', 'resBuildMaxHeap5.csv', \
               'resBuildMaxHeap6.csv', 'resBuildMaxHeap7.csv', 'resBuildMaxHeap8.csv', 'resBuildMaxHeap9.csv', 'resBuildMaxHeap10.csv']
csvfilesInsertion = ['resInsertionSort1.csv', 'resInsertionSort2.csv', 'resInsertionSort3.csv', 'resInsertionSort4.csv', 'resInsertionSort5.csv', \
               'resInsertionSort6.csv', 'resInsertionSort7.csv', 'resInsertionSort8.csv', 'resInsertionSort9.csv', 'resInsertionSort10.csv']
csvcontainer = []
csvcontainer.append(csvfilesHeap)
csvcontainer.append(csvfilesInsertion)

tablestoplot = []

for container in csvcontainer:

    # Table to store array of csvfiles data
    tables = []

    # Table which will be populated by average of each table element
    tabletoplot = []

    for csvfile in container:
        print("\nReading csv: " + csvfile)

        # Opens CSV and stores data into a table
        csvtable = CSVHelper.readFile(csvfile, delimiter=delimiter)

        # Append to tables
        tables.append(csvtable)

        # Prints read data to console
        print("---\n" + str(csvtable))


    print("Total iterations: " + str(tables[0][-1]['Iteration']))

    length = int(tables[0][-1]['Iteration']) - 1

    for index in range(0, length):
        print("index: " + str(index))
        valuestoaverage = []

        # Calculating average of yaxis values
        for table in tables:
            valuestoaverage.append(table[index][yaxis])

        print("\nCalculating average of: " + str(valuestoaverage))

        # Calculating average 
        partialaverage = 0
        for value in valuestoaverage:
            partialaverage += float(value)
        average = partialaverage / len(valuestoaverage)

        print("Average is: " + str(average))

        # appending to new table to plot
        newentry = {}
        newentry[yaxis] = average
        newentry[xaxis] = table[index][xaxis]   # xaxis has not changed, take it from whatever table

        # Appending to table to plot
        tabletoplot.append(newentry)


    if len(tabletoplot) == 0:
        print("An error occurred when loading data")
        sys.exit(1)

    tablestoplot.append(tabletoplot)


print("Generating plots ...")

print("\nPlottiing table: \n" + str(tablestoplot[0]) + '\n' + str(tablestoplot[1]))
# Plot using PlotHelper
PlotHelper.plotcsvmetric(tablestoplot[0], xaxis, yaxis, figuretitle[0], unitofmeasure, False)
PlotHelper.plotcsvmetric(tablestoplot[0], xaxis, yaxis, figuretitle[1], unitofmeasure, False, tablestoplot[1])

# print("\nPNG Graph saved in " + dirname)
