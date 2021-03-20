# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:03:23 2021

@author: Egemen G
"""

import pandas as pd
import cv2 as cv
from sklearn.cluster import k_means
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

# CONVERT BGR TO HSV FORMAT
# RESIZE IMAGE DIMENSIONS
          

def get_image(image_path):

    img = cv.imread(image_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)        
    img = cv.resize(img, (800,100), interpolation=cv.INTER_AREA)
    plt.imshow(img)
    img = img.reshape(img.shape[0]*img.shape[1], 3)
    
    return img

# CONVERT TO HEX CODE
def RGB2HEX(color):
    
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
conc = []
gang = []
# CLUSTERING 
def get_colors(image, cluster_numbers):
    
    km = KMeans(n_clusters=cluster_numbers)
    colors = km.fit_predict(image)  
    for i in colors:
        if i == 0:
            conc.append(i)
        else:
            gang.append(i)
    counts = Counter(colors)
    center_colors = km.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    
    plt.figure(figsize=(8,6))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
    plt.show()

    
image = get_image("img_path")
get_colors(image,2)


