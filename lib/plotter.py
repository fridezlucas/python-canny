""" Plotter module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def erase2RGBValues(image, v1, v2):

    rImage = np.array(image, copy=True)

    for y in rImage:
        for x in y:
            x[v1] = 0
            x[v2] = 0
    
    return rImage

def plotImageRGB(image):

    img = mpimg.imread(image)

    figure, axes = plt.subplots(nrows=2, ncols=2)

    plt.suptitle("Analyse RGB image")
    axes[0,0].set_title("Original image")
    axes[0,0].imshow(img)

    axes[0,1].set_title("Original image R")
    axes[0,1].imshow(erase2RGBValues(img, 1, 2))

    axes[1,0].set_title("Original image G")
    axes[1,0].imshow(erase2RGBValues(img, 0, 2))

    axes[1,1].set_title("Original image B")
    axes[1,1].imshow(erase2RGBValues(img, 0, 1))

    figure.tight_layout()
    plt.show()