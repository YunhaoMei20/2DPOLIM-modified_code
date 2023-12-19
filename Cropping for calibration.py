# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:02:50 2023

@author: 54112
"""

import os
import numpy as np
import pandas as pd
import tifffile as tiff

# Define the folder path
folder_path = r"E:\download\WGtest\15_90"

# Create empty lists to store the intensity values
I1_list, I2_list, I3_list, I4_list = [], [], [], []

# Loop through each TIF image in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".tif"):
        # Load the TIF image
        image_path = os.path.join(folder_path, filename)
        image = tiff.imread(image_path)
        
        # Extract the four regions and calculate the average intensity of each region
        # region1 = image[708:873, 825:936]
        # I1 = np.mean(region1)
        # I1_list.append(I1)
        
        # region2 = image[78:987, 1959:2055]
        # I2 = np.mean(region2)
        # I2_list.append(I2)
        
        # region3 = image[1082:1247, 825:936]
        # I3 = np.mean(region3)
        # I3_list.append(I3)
        
        # region4 = image[1075:1984, 1952:2018]
        # I4 = np.mean(region4)
        # I4_list.append(I4)
        x1=50
        y1=896
        w1=696
        h1=792
        x2=50
        y2=1947
        w2=696
        h2=60
        x3=1287
        y3=894
        x4=1287
        region1 = image[int(y1):int(y1+h1), int(x1):int(x1+w1)]
        I1 = np.mean(region1)
        I1_list.append(I1)
        
        region2 = image[int(y2):int(y2+h2), int(x2):int(x2+w2)]
        I2 = np.mean(region2)
        I2_list.append(I2)
        
        region3 = image[int(y3):int(y3+h1), int(x3):int(x3+w1)]
        I3 = np.mean(region3)
        I3_list.append(I3)
        
        region4 = image[int(y2):int(y2+h2), int(x4):int(x4+w2)]
        I4 = np.mean(region4)
        I4_list.append(I4)
# print("Average intensity of region 1: ", I1_list)
# print("Average intensity of region 2: ", I2_list)
# print("Average intensity of region 3: ", I3_list)
# print("Average intensity of region 4: ", I4_list)
# Calculate M and N values
M = np.array(I1_list) - np.array(I2_list)
N = np.array(I3_list) - np.array(I4_list)

# Create a Pandas DataFrame to store the results
data = {"Filename": os.listdir(folder_path), "L": M, "R": N}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file with the folder name as the filename
excel_path = os.path.join(folder_path, folder_path.split("/")[-1] + ".xlsx")
df.to_excel(excel_path, index=False)