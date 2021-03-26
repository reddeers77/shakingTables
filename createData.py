# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 02:33:44 2021

@author: Egemen G
"""

import pandas as pd
import numpy as np
import tensorflow as tf
import keras
import csv
import matplotlib.pyplot as plt


class shakingTable():


    def __init__(self, conc, mid, gang, conc_size, mid_size, data_size):
        self.conc = [10,9,9]
        self.mid = [74,49,49]
        self.gang = [136,106,105]
        self.conc_size = 20
        self.mid_size = 30
        self.data_size = 100
    


    def createData(self):
        data = []
        for c in range( 1, conc_size+1 ) :    
            for m in range( 0, mid_size+1 ):
                frames = [gang]*100
                frames = np.array(frames)        
                frames[:c,] = conc
                frames[c:c+m,] = mid        
                data.append(frames)
        return data


####################    PLOT DATA    ####################

def showData(data):

    for i in range(0,len(data)):
        plt.imshow(data[i])
        plt.show()

####################    SAVE DATA    ####################   
 
def saveData(path,data):
    with open( path+".csv", 'w', newline='' ) as csvfile:
        writer = csv.writer(csvfile)        
        writer.writerows(data)
        return True
    
####################    LOAD DATA    ####################

def loadData(path):
    delete = ["", " ","[","]","[ "," ]","''"]
    loadedData = pd.read_csv(path+".csv",header=None)
    # Prepare single cell in data
    rows,cols = loadedData.shape[0],loadedData.shape[1]

    for row in range(0,rows):
    
        for col in range(0,cols):
            cell = loadedData[col][row] # take cell
            cell = cell.split(" ") # split it
            
            newCell = []
            
            for i in cell:
                if not (i in delete):
                    newCell.append(i)
                else:
                    continue
            cell = newCell
            for j in range(0,3): #take the cell
                cell[j] = cell[j].replace("[","") # delete ] from cell
                cell[j] = cell[j].replace("]","") #  delete [ from cell
                cell[j] = cell[j].replace(" ","")
                cell[j] = int(cell[j]) # render it integer
               
            loadedData[col][row] = cell            
#convert every df to np.array (100,3),  all data in the frames list   
    frames = []
    l = []
    for j in range(0,rows):
        for i in range(0,cols):
            cell = loadedData.iloc[j,i]
            l.append(cell)
            if i == (cols-1):
                l = np.array(l)
                frames.append(l)
                l = []
    return frames    

    
path = ".../dataPrep"
conc = [10,9,9]
mid = [74,49,49]
gang = [136,106,105]

data_size = 100
conc_size = 3
mid_size = 2

new = shakingTable(conc,mid,gang,conc_size,mid_size,data_size)
cccc = new.createData()
saveData(path,cccc)
a = loadData(path)
showData(a)
