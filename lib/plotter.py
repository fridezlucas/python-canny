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
    """ Erase 2 RGB values (set to 0)

    v1 : index value 1 to reset
    v2 : index value 2 to reset

    return : image converted
    """

    img = np.array(image, copy=True)

    for y in img:
        for x in y:
            x[v1] = 0
            x[v2] = 0

    return img


def getBlackWhiteImage(image):
    """ Get an image in grayscale

    image  : Image to convert to grayscale
    return : new image in grayscale
    Source : https://kite.com/python/answers/how-to-convert-an-image-from-rgb-to-grayscale-in-python
    """

    img = np.array(image, copy=True)

    rgb_weights = [0.299, 0.587, 0.114]
    grayscale_image = np.dot(img[..., :3], rgb_weights)

    return grayscale_image


def plotGrayscaleImage(image):
    """ Plot an image in grayscale

    image : image to plot in grayscale
    """
    img = mpimg.imread(image)

    plt.figure(1)
    plt.suptitle("Grayscale image")
    plt.imshow(getBlackWhiteImage(img), cmap=plt.get_cmap("gray"))
    plt.show()


def plotImageRGB(image):
    """Plot an image in 4 variants (original, R, G, B)

    image : Image to plot
    """

    img = mpimg.imread(image)

    figure, axes = plt.subplots(nrows=2, ncols=2)

    plt.suptitle("Analyse RGB image")
    axes[0, 0].set_title("Original image")
    axes[0, 0].imshow(img)

    axes[0, 1].set_title("Original image R")
    axes[0, 1].imshow(erase2RGBValues(img, 1, 2))

    axes[1, 0].set_title("Original image G")
    axes[1, 0].imshow(erase2RGBValues(img, 0, 2))

    axes[1, 1].set_title("Original image B")
    axes[1, 1].imshow(erase2RGBValues(img, 0, 1))

    figure.tight_layout()
    plt.show()
