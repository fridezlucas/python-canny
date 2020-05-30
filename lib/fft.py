""" FFT Image calculator module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.05.13
Version : 1.0
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def fftImage(image):
    """Calculate fft of image

    Return : fft Image
    """
    return abs(np.fft.fft2(image))
