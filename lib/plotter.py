""" Plotter module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image


def erase2Values(image, v1, v2):
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

    plt.figure("Plot 3/3 : Grayscale image")
    plt.suptitle("Grayscale image")
    plt.imshow(getBlackWhiteImage(img), cmap=plt.get_cmap("gray"))
    plt.show()


def plotImageRGB(image):
    """Plot an image in 4 variants (original, R, G, B)

    image : Image to plot
    """

    img = mpimg.imread(image)

    figure, axes = plt.subplots(nrows=2, ncols=2)
    figure.canvas.set_window_title("Plot 1/3 : Image RGB")

    plt.suptitle("Analyse RGB image")
    axes[0, 0].set_title("Original image")
    axes[0, 0].imshow(img)

    axes[0, 1].set_title("Image R values")
    axes[0, 1].imshow(erase2Values(img, 1, 2))

    axes[1, 0].set_title("Image G values")
    axes[1, 0].imshow(erase2Values(img, 0, 2))

    axes[1, 1].set_title("Image B values")
    axes[1, 1].imshow(erase2Values(img, 0, 1))

    figure.tight_layout()
    plt.show()

def plotImageCMY(image):
    figure, axes = plt.subplots(nrows=2, ncols=2)
    figure.canvas.set_window_title("Plot 2/3 : Image CMY")

    img = Image.open(image)

    plt.suptitle("Analyse RGB image")
    axes[0, 0].set_title("Original image")
    axes[0, 0].imshow(img)

    img = np.asarray(Image.open(image).convert("CMYK"))

    axes[0, 1].set_title("Image C values")
    axes[0, 1].imshow(Image.fromarray(np.uint8(erase2Values(img, 1, 2)), mode="CMYK"))

    axes[1, 0].set_title("Image M values")
    axes[1, 0].imshow(Image.fromarray(np.uint8(erase2Values(img, 0, 2)), mode="CMYK"))

    axes[1, 1].set_title("Image Y values")
    axes[1, 1].imshow(Image.fromarray(np.uint8(erase2Values(img, 0, 1)), mode="CMYK"))

    figure.tight_layout()
    plt.show()

def plotAll(image):
    """ Plot all variants with image given

    image : image to plot in multiple variants
    """
    plotImageRGB(image)
    plotImageCMY(image)
    plotGrayscaleImage(image)
