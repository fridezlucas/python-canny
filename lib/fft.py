""" FFT Image calculator module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.05.13
Version : 1.0
"""

import os
import glob
import sys


def getAllFiles(dir):
    """ Get all images files

    Only keep images files (*.png *.jpg *.jpeg)
    """

    fileExtensions = ("*.png", "*.jpeg", "*.jpg", "*.gif")

    listFiles = []
    for files in fileExtensions:
        listFiles.extend(glob.glob(f"{dir}/{files}"))

    return listFiles


def fftImage(image):
    """Calculate fft of image

    Return : fft Image
    """
    pass
