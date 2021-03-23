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

####################    CREATE DATA AND SAVE    ####################

conc = [139, 231, 104]
gang = [247, 22, 18 ]

data = []
data_size = 100
i = 0
while i<101:
    frames = [conc]*data_size
    frames=np.array(frames)
    new = frames
    new[:i,] = gang
    data.append(new)
    i+=1
    
data = np.array(data)

with open("path/dataPrep.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
  
####################    LOAD DATA    ####################
a = pd.read_csv("path/dataPrep.csv",header=None)
# Prepare single cell in data


for row in range(0,101):
    
    for i in range(0,100):
        cell = a[i][row] # take cell
        cell = cell.split(" ") # split it
    
        if ( len(cell)==5):                   
            del cell[1:4:2] # delete the spaces        
            print(cell)

        for j in range(0,3): #take the cell
            cell[j] = cell[j].replace("[","") # delete ] from cell
            cell[j] = cell[j].replace("]","") #  delete [ from cell
            cell[j] = int(cell[j]) # render it integer
    
        a[i][row] = cell

####################    convery every df to np.array (100,3), all data in the frames list    ####################
frames = []
l = []
for j in range(0,101):
    for i in range(0,100):
        cell = a.iloc[j,i]
        l.append(cell)
        if i ==99:
            l = np.array(l)
            frames.append(l)
            l = []

# plot data flatt
"""
model = keras.Sequential(keras.layers.Flatten(input_shape=(100,3)))
for i in range(0,101):
    batch= tf.expand_dims(frames[i], [0])
    img = model.predict(batch)
    plt.ylim(0,10)
    plt.imshow(img)
    plt.show()
"""
####################    PLOT DATA    ####################
for i in range(0,len(frames)):
    plt.imshow(frames[i])
    plt.show()
