""" Canny module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.28
Version : 1.0
"""

import numpy as np
from scipy import ndimage
from scipy.ndimage.filters import convolve
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import scipy.misc as sm


def gaussian_kernel(size, sigma=1):
    """ Get Gaussian filter for image   

    Reduce noise on image to do a better Edge detection
    size  : image size
    sigma : parameter in equation (default = 1)

    Return : Gaussian Kernel
    """

    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g = np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g


def sobel_filters(img):
    """ Detect edge intensity with gradient vectors

    img : image to analyze

    Return : Gradient and angle
    """

    # sobel filters for each direction (x; y)
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    # Apply filters
    Ix = ndimage.filters.convolve(img, Kx)
    Iy = ndimage.filters.convolve(img, Ky)

    # Get magnitude G and slope theta of gradient
    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)

    return (G, theta)


def non_max_suppression(img, D):
    """ Delete all non max value according to gradient

    Only edge will be kept

    Return : Non zero image
    """
    M, N = img.shape
    Z = np.zeros((M, N), dtype=np.int32)
    alpha = D * 180. / np.pi
    alpha[alpha < 0] += 180

    # Suppress each non max value
    for i in range(1, M-1):
        for j in range(1, N-1):
            try:
                q = 255
                r = 255

               # angle 0
                if (0 <= alpha[i, j] < 22.5) or (157.5 <= alpha[i, j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                # angle 45
                elif (22.5 <= alpha[i, j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                # angle 90
                elif (67.5 <= alpha[i, j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                # angle 135
                elif (112.5 <= alpha[i, j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                # Apply weak/strong selection
                if (img[i, j] >= q) and (img[i, j] >= r):
                    Z[i, j] = img[i, j]
                else:
                    Z[i, j] = 0

            except IndexError as e:
                pass

    return Z


def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    """ Apply double threshold filter

    High treshold is used to identify strong pixel
    Low treshold is used to identify weak pixel

    img : image to analyze
    lowThresholdRatio : Ratio for low threshold
    highThresholdRatio : Ratio for high threshold

    Return : result image
    """
    highThreshold = img.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio

    M, N = img.shape
    res = np.zeros((M, N), dtype=np.int32)

    weak = np.int32(25)
    strong = np.int32(255)

    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)

    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak

    return (res, weak, strong)


def hysteresis(img, weak, strong=255):
    """
    Transform weak pixel inot strong one only if weak pixel is surrounded by strong ones

    img    : image to analyse
    weak   : weak value to remove
    strong : strong value

    Return image after hysteresis filter
    """
    
    img = img[0]
    M, N = img.shape
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i, j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                            or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass

    return img


def canny(image):
    """ Detect edge for an image

    image : image to analyse and detect edges
    return : edge image

    Return : All image steps
    """
    img_smoothed = convolve(image, gaussian_kernel(5, 1))
    gradientMat, thetaMat = sobel_filters(img_smoothed)
    nonMaxImg = non_max_suppression(gradientMat, thetaMat)
    thresholdImg = threshold(nonMaxImg)
    img_final = hysteresis(thresholdImg, 25)

    return [gradientMat, nonMaxImg, img_final]
