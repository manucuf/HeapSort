#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np


def plotcsvmetric(csvtable, xaxis, parameter, figuretitle, unitofmeasure, displayaverage, secondtable = None):
    # Plots the paramter variation in domain specified by timeaxis
    # Calculates average
    # Saves plot as .png file

    # Getting start and end
    starttime = float(csvtable[0][xaxis])
    endtime = float(csvtable[-1][xaxis])

    # Getting step from delta interval between first consecutive samples
    step = float(csvtable[1][xaxis]) - float(csvtable[0][xaxis])

    # Creating x axis
    x = np.arange(starttime, endtime + 1, step)

    # Define figure
    fig, ax = plt.subplots(figsize=(7, 7))

    # Build data array for selected parameter
    dataarray = []

    for row in csvtable:
        data = float(row[parameter])
        dataarray.append(data)

    npdataarray = np.array(dataarray)

    npx = np.linspace(0, x[-1], len(dataarray))
    
    # Calculating average
    average = np.average(npdataarray)

    # Second parameter
    dataarray2 = []
    if secondtable is not None:
        for row in secondtable:
            data = float(row[parameter])
            dataarray2.append(data)

    npdataarray2 = np.array(dataarray2)

    # Plot, labeling and options

    ax.plot(npx, npdataarray, label='HeapSort average trend', color='blue')
    # Same class function
    ax.plot(npx, 1e-08*npx*np.log2(npx), label="O(n*log2(n)) function", color='green')

    if (secondtable is not None):
        ax.plot(npx, npdataarray2, label='InsertionSort average trend', color='orange')
        # Same class function
        ax.plot(npx, 0.28e-09*np.power(npx, 2), label="O(n^2) function", color='purple')

    if (displayaverage == True):
        ax.set(xlabel=xaxis, ylabel=unitofmeasure, title = figuretitle + '\n\nAverage = ' + str(average))
    else:
        ax.set(xlabel=xaxis, ylabel=unitofmeasure, title = figuretitle)
    ax.grid()
    ax.legend(loc='upper left')

    # Saving PNG
    fig.savefig(figuretitle + ".png")

    # Show figure
    plt.show()


# def plotcdf(csvtablemac, csvtableip, packetsize, packetrate, figuretitle, unitofmeasure):

#     # print("MAC:\n" + str(csvtablemac))
#     # print("IP:\n" + str(csvtableip))

#     # array to store data
#     dataarraymac = []
#     dataarrayip = []
#     dataarrayipsent = []

#     for row in csvtablemac:
#         data = float(row['inter_packet_time'])

#         if data < 1:
#             dataarraymac.append(data)

#     for row in csvtableip:
#         data = float(row['inter_packet_time'])

#         if data < 1:
#             dataarrayip.append(data)

#     # ** AVOID DIMENSION MISMATCH POSSIBILITES **

#     # Remove exceeding samples
#     # if len(dataarrayip) > len(dataarraymac):
#     #     elemtoremove = len(dataarrayip)-len(dataarraymac)
#     #     dataarrayip = dataarrayip[:(len(dataarrayip)-elemtoremove)]
#     # elif len(dataarraymac) > len(dataarrayip):
#     #     elemtoremove = len(dataarraymac)-len(dataarrayip)
#     #     dataarraymac = dataarraymac[:(len(dataarraymac)-elemtoremove)]

#     # Add 0 padding to have same sample numbers
#     # if len(dataarrayip) > len(dataarraymac):
#     #     for index in range(len(dataarraymac), len(dataarrayip)):
#     #         dataarraymac.append(0)
#     # elif len(dataarraymac) > len(dataarrayip):
#     #     for index in range(len(dataarrayip), len(dataarraymac)):
#     #         dataarrayip.append(0)

#     # ** **

#     # Add interpacket at generation
#     interpacketgenerated = 1/float(packetrate)
#     for i in range(0, len(dataarrayip)):
#         dataarrayipsent.append(interpacketgenerated)

#     # convert to numpy array
#     numpyarraymac = np.array(dataarraymac)
#     numpyarrayip = np.array(dataarrayip)
#     numpyarrayipsent = np.array(dataarrayipsent)

#     # sort to build x axis
#     x1 = np.sort(numpyarraymac)
#     x2 = np.sort(numpyarrayip)
#     x3 = np.sort(numpyarrayipsent)

#     # Normalization
#     numpyarraymac /= numpyarraymac.sum()
#     numpyarrayip /= numpyarrayip.sum()
#     numpyarrayipsent /= numpyarrayipsent.sum()

#     # Cumulative function
#     cdfmac = np.cumsum(numpyarraymac)
#     cdfip = np.cumsum(numpyarrayip)
#     cdfipsent = np.cumsum(numpyarrayipsent)

#     # Define figure
#     fig, ax = plt.subplots(figsize=(5, 5))

#     # Plot, labeling and options
#     ax.plot(x2, cdfip, label='Interpacket Time IP Level Received', color='red')
#     ax.plot(x1, cdfmac, label='Interpacket Time MAC Level UE side', color='green')
#     ax.plot(x3, cdfipsent, label='Interpacket Time IP Level UE side', color='blue')
#     ax.legend(loc='lower right')  # upper right, upper left, lower right, lower left

#     ax.set(xlabel='seconds', ylabel=unitofmeasure, title=figuretitle)
#     ax.grid()

#     # Saving PNG
#     fig.savefig("results/comparison_cdf.png")

#     # Show figure
#     plt.show()


# def doubleplot(iptable, mactable, figuretitle, unitofmeasure):


#     # Build data array for selected parameter
#     macarray = []  # 1
#     iparray = []  # 2

#     for row in mactable:
#         data = float(row['ul_brate'])
#         data = data/1000000
#         macarray.append(data)

#     for row in iptable:
#         data = float(row['throughput'])
#         data = data/1000
#         iparray.append(data)

#     # print("mactable lenght: " + str(len(macarray)) + ", iptable lenght: " + str(len(iparray)))

#     # Add 0 padding to have same sample numbers
#     if len(iparray) > len(macarray):
#         for index in range(len(macarray), len(iparray)):
#             macarray.append(0)
#     elif len(macarray) > len(iparray):
#         for index in range(len(iparray), len(macarray)):
#             iparray.append(0)

#     # print("After alignment - mactable lenght: " + str(len(macarray)) + ", iptable lenght: " + str(len(iparray)))

#     # Data for plotting
#     starttime = 0.0
#     endtime = float(len(macarray))
#     step = 1
#     t = np.arange(starttime, endtime, step)

#     # Define figure
#     fig, ax = plt.subplots(figsize=(7, 3))

#     # Calculating average
#     notzerodata1 = []
#     for data in macarray:
#         if float(data) != 0.0:
#             notzerodata1.append(data)
#     average1 = np.average(notzerodata1)

#     notzerodata2 = []
#     for data in iparray:
#         if float(data) != 0.0:
#             notzerodata2.append(data)
#     average2 = np.average(notzerodata2)

#     # Plot, labeling and options
#     ax.plot(t, macarray, label="MAC Level UE side")
#     ax.plot(t, iparray, label="IP Level Received")

#     ax.set(xlabel='time (s)', ylabel=unitofmeasure, title=figuretitle + '\n\nAverage MAC = ' + str(average1) + ', Average IP = ' + str(average2))
#     ax.legend(loc='upper left')  # upper right, upper left, lower right, lower left
#     ax.grid()

#     # Saving PNG
#     fig.savefig("results/" + "_comparison_analysis.png")

#     # Show figure
#     plt.show()
