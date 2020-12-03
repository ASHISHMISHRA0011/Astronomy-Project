#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:24:46 2020

@author: dev
"""

import math
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import (line, polygon, disk,
                          circle_perimeter,
                          ellipse, ellipse_perimeter,
                          bezier_curve)


x=np.arange(np.deg2rad(0),np.deg2rad(180),np.deg2rad(0.2))
z = np.cos(x)
y=x*180/np.pi

with open('label.txt', 'w') as file:
    for data in z:
        file.write(str(data)+'\n')

for i in range(len(x)):
    img = np.zeros((500, 500, 3), dtype=np.double)
    rr, cc = ellipse(250, 250, 100, 200, rotation=x[i])
    img[rr, cc, :] = 1
    plt.axis('off')
    
    plt.imsave('{}.png'.format(i),img)
    plt.imshow(img)
    
    
    
    
