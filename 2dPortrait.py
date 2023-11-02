# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:51:29 2023
This is only for generate 2D Polarization Portrait, the cos^2 fitting I use origin. I will update the code for automatic fitting.
@author: Yunhao
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sp  # Import the scipy.ndimage module for Gaussian filtering
from sklearn.preprocessing import MinMaxScaler
import cv2

# Define the x and y values for the two given datasets
x1 = np.array([0, 30, 60, 90, 120, 150, 180])
x2 = np.array([0, 45, 90, 135, 180])
y1 = np.array([425.46806, 318.05782, 114.74271, 7.61028, 107.13312, 311.13547, 425.46806])
y2 = np.array([899.70481, 385.022, 1.29735E-4, 424.88858, 899.70481])

# Normalize y1
y1_min = np.min(y1)
y1_max = np.max(y1)
y1 = (y1 - y1_min) / (y1_max - y1_min)

# Normalize y2
y2_min = np.min(y2)
y2_max = np.max(y2)
y2 = (y2 - y2_min) / (y2_max - y2_min)

# Create new arrays to store x values in the range [0, 180] with a step of 1
x1_new = np.arange(0, 181)
x2_new = np.arange(0, 181)

# Use linear interpolation to calculate new y values based on the given x and y values
y1_new = np.interp(x1_new, x1, y1)
y2_new = np.interp(x2_new, x2, y2)

# Create a two-dimensional array to store the sum of y values from both datasets
z = np.zeros((len(x2_new), len(x1_new)))

# Iterate through the two-dimensional array to calculate values for each position
for i in range(len(x2_new)):
    for j in range(len(x1_new)):
        z[i, j] = y2_new[i] + y1_new[j]

# Apply Gaussian filtering to the two-dimensional array with a standard deviation of 5
z_smooth = sp.gaussian_filter(z, sigma=5)

# Create a plot object
fig, ax = plt.subplots()

# Use imshow to plot the smoothed heatmap with the "jet" colormap and add a color bar
im = ax.imshow(z_smooth, cmap="jet")
cbar = fig.colorbar(im)

# Set labels for the x and y axes
plt.xlabel(r'$\phi_{ex}$', fontsize=12)
plt.ylabel(r'$\phi_{em}$', fontsize=12)

# Set the tick positions and labels for the x and y axes
ax.set_xticks(np.arange(0, 181, 30))
ax.set_yticks(np.arange(0, 181, 30))
ax.set_xticklabels(np.arange(0, 181, 30))
ax.set_yticklabels(np.arange(0, 181, 30))

# Add text annotations to the right of the color bar
x1 = x1_new[np.argmax(y1)]
x2 = x2_new[np.argmax(y2)]
x1 = round(x1, 3)
x2 = round(x2, 3)
LS = x2 - x1
M_ex = (max(y1) - min(y1)) / (max(y1) + min(y1))
M_em = (max(y2) - min(y2)) / (max(y2) + min(y2))
LS = round(LS, 3)
M_ex = round(M_ex, 3)
M_em = round(M_em, 3)
# Calculate the x- and y-coordinate for displaying the text on the right
cbar_pos = cbar.ax.get_position()
text_x = cbar_pos.xmax + 280
text_y = np.arange(150, 10, -30)
# Display the text, and specify the color and font size
# plt.text(text_x, text_y[0], r'$\theta_{em}=$' + str(x1), color='black', fontsize=12)
# plt.text(text_x, text_y[1], r'$\theta_{ex}=$' + str(x2), color='black', fontsize=12)
# plt.text(text_x, text_y[2], f'$LS={LS}$', color='black', fontsize=12)
# plt.text(text_x, text_y[3], r'$M_{ex}=$' + str(M_ex), color='black', fontsize=12)
# plt.text(text_x, text_y[4], r'$M_{em}=$' + str(M_em), color='black', fontsize=12)
plt.text(text_x, text_y[0], r'$\theta_{em}=-0.016$', color='black', fontsize=12)
plt.text(text_x, text_y[1], r'$\theta_{ex}=-0.127$', color='black', fontsize=12)
plt.text(text_x, text_y[2], f'LS = -0.111', color='black', fontsize=12)
plt.text(text_x, text_y[3], r'$M_{ex}=0.963$', color='black', fontsize=12)
plt.text(text_x, text_y[4], r'$M_{em}=0.997$', color='black', fontsize=12)

# Set the title of the plot
ax.set_title("Artificial Molecule Set at 1 Degree")
ax.invert_yaxis()

# Save the plot to an image file and display it
plt.savefig("2Dportrait_am001.png", bbox_inches='tight', dpi=300)
plt.show()
