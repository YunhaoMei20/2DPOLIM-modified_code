# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:47:37 2023

@author: 54112
"""
# Import the necessary libraries
import numpy as np
import cv2
import glob

# Define the paths where your dark frames and flat frames are stored
dark_path = "E:/download/231004/231004/dfg/dark"
flat_path = "E:/download/231004/231004/dfg/light"
sample_path = "C:/Users/54112/Desktop/data/master thesis/230621/sample"

# Use the glob module to get a list of all the dark frame files in the path
dark_files = glob.glob(dark_path + "/*.tif") # Change .fit to .tiff
dark_data = []
for file in dark_files: 
    dark_data.append(cv2.imread(file, cv2.IMREAD_UNCHANGED))
dark_data = np.array(dark_data)
master_dark = np.mean(dark_data, axis=0)
cv2.imwrite("master_dark.tif", master_dark) # Change .fit to .tiff

# Use the glob module to get a list of all the flat frame files in the path
flat_files = glob.glob(flat_path + "/*.tif") # Change .fit to .tiff
flat_data = []
for file in flat_files: 
    flat_data.append(cv2.imread(file, cv2.IMREAD_UNCHANGED))
flat_data = np.array(flat_data)
master_flat = np.mean(flat_data, axis=0)
cv2.imwrite("master_flat.tiff", master_flat) # Change .fit to .tiff

# Use the cv2 module to read the image data of the master dark frame and the master flat field as numpy arrays
D = cv2.imread(dark_path + "/master_dark.tif", cv2.IMREAD_UNCHANGED) # Change .fit to .tiff
F = cv2.imread(flat_path + "/master_flat.tif", cv2.IMREAD_UNCHANGED) # Change .fit to .tiff

# Use the cv2 module to read the image data of the sample photo as a numpy array
T = cv2.imread(sample_path + "/1_00003.tif", cv2.IMREAD_UNCHANGED)

# Convert the data type of T, D, and F to float32
T = T.astype(np.float32)
D = D.astype(np.float32)
F = F.astype(np.float32)

# Apply the final picture formula to calculate P
P = np.subtract(np.divide(T, np.subtract(F, D)), np.divide(D, np.subtract(F, D)), dtype=np.uint16)

# Save the final picture P as a new TIFF file using the cv2 module
cv2.imwrite("final_picture.tif", P)
