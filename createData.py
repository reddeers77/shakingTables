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
        self.conc = conc
        self.mid = mid
        self.gang = gang
        self.conc_size = conc_size
        self.mid_size = mid_size
        self.data_size = data_size
        
    def info(self):
        print("Concentration color: "+str(self.conc))
        print("Middling color: "+str(self.mid))
        print("Gangue color: "+str(self.gang))
        print("Concentration Size: "+str(self.conc_size))
        print("Middling Size: "+str(self.mid_size))
        
    def createData(self):
        self.data = []
        for c in range( 1, self.conc_size+1 ) :    
            for m in range( 0, self.mid_size+1 ):
                frames = [self.gang]*100
                frames = np.array(frames)        
                frames[:c,] = self.conc
                frames[c:c+m,] = self.mid        
                self.data.append(frames)
        return self.data
    
    def sliderPoints(self):
        points = []
        for c in range (1, self.conc_size+1):
            for m in range (0, self.mid_size+1):
                new_point = [c,(c+m)]
                if ( c == (c+m)):
                    new_point = [c,0]
                                   
                points.append(new_point)
        return points
    
    def ratios(self):
        c_perc =(self.conc_size/self.data_size)*100
        m_perc = (self.mid_size/self.data_size)*100
        g_perc = ((self.data_size-(c_perc+m_perc))/self.data_size)*100
        
        print("Concentration percentage : % "+str(c_perc))
        print("Middling percentage : % "+str(m_perc))
        print("Gangue percentage : % "+str(g_perc))
        return c_perc, m_perc, g_perc

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

   
path = "..../dataPrep"
conc = [10,9,9]
mid = [74,49,49]
gang = [136,106,105]

data_size = 100
conc_size = 10
mid_size = 5

table1 = shakingTable(conc,mid,gang,conc_size,mid_size,data_size) # Create a new shakingTable Object
table1.info() # Shows infos about table flow                                        
table1.ratios() # Show flows ratios
table_pictures = table1.createData() # Create RGB values of the each flows
points = table1.sliderPoints() # Shows the corresponding values of slider points of each flow times

saveData(path,table_pictures) # Saves data to defined path file and name as .csv file
loaded_pictures = loadData(path) # Load data from saves .csv file
showData(loaded_pictures) # shows each flow times in pylot graph 

