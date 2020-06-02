""" Plotter module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

from lib.canny import canny
from lib.fft import fftImage


def erase2Values(image, v1, v2, value=0):
    """ Erase 2 RGB values (set to 0)

    v1 : index value 1 to reset
    v2 : index value 2 to reset

    Return : image converted
    """

    img = np.array(image, copy=True)

    for y in img:
        for x in y:
            x[v1] = value
            x[v2] = value

    return img


def getBlackWhiteImage(image):
    """ Get an image in grayscale

    image  : Image to convert to grayscale  
    Return : new image in grayscale
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

    plt.figure("Step 3/5 : Grayscale image")
    plt.suptitle("Grayscale image")
    plt.imshow(getBlackWhiteImage(img), cmap=plt.get_cmap("gray"))
    plt.show()


def plotImageRGB(image):
    """Plot an image in 4 variants (original, R, G, B)

    image : Image to plot
    """

    img = mpimg.imread(image)

    figure, axes = plt.subplots(nrows=2, ncols=2)
    figure.canvas.set_window_title("Step 1/5 : Image RGB")

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
    """Plot an image in 4 variants (original, C, M, Y)

    image : Image to plot
    """
    img = mpimg.imread(image)

    figure, axes = plt.subplots(nrows=2, ncols=2)
    figure.canvas.set_window_title("Step 2/5 : Image CMY")

    plt.suptitle("Analyse CMY image")
    axes[0, 0].set_title("Original image")
    axes[0, 0].imshow(img)

    print(img[0][0])

    axes[0, 1].set_title("Image C values")
    axes[0, 1].imshow(erase2Values(img, 1, 2, 1))

    axes[1, 0].set_title("Image M values")
    axes[1, 0].imshow(erase2Values(img, 0, 2, 1))

    axes[1, 1].set_title("Image Y values")
    axes[1, 1].imshow(erase2Values(img, 0, 1, 1))

    figure.tight_layout()
    plt.show()


def plotImageCanny(image):
    """Plot an image with Canny

    image : Image to plot
    """

    figure, axes = plt.subplots(nrows=2, ncols=2)
    figure.canvas.set_window_title("Canny")

    img = mpimg.imread(image)

    plt.suptitle("Step 4/5 : Canny Edge detectors")
    axes[0][0].set_title("Original image [1/4]")
    axes[0][0].imshow(img)

    imgCanny = canny(getBlackWhiteImage(img))

    axes[0][1].set_title("Gradient image [2/4]")
    axes[0][1].imshow(imgCanny[0], cmap=plt.get_cmap("gray"))

    axes[1][0].set_title("Non max [3/4]")
    axes[1][0].imshow(imgCanny[1], cmap=plt.get_cmap("gray"))

    axes[1][1].set_title("Edge detected [4/4]")
    axes[1][1].imshow(imgCanny[2], cmap=plt.get_cmap("gray"))

    figure.tight_layout()
    plt.show()

def plotImageFFT(image):
    """Plot an image FFT

    image    : Image to plot
    imageFFT : Image FFT to plot
    canny    : Image canny to plot
    cannyFFT : Image Canny FFT to plot
    """

    figure, axes = plt.subplots(nrows=2, ncols=2)
    figure.canvas.set_window_title("FFT")

    img = mpimg.imread(image)

    plt.suptitle("Step 5/5 : Canny Edge detectors")
    axes[0][0].set_title("Original image")
    axes[0][0].imshow(img)

    imgCanny = canny(getBlackWhiteImage(img))

    axes[0][1].set_title("FFT original image")
    axes[0][1].imshow(fftImage(img))

    axes[1][0].set_title("Canny image")
    axes[1][0].imshow(imgCanny[2], cmap=plt.get_cmap("gray"))

    axes[1][1].set_title("FFT Canny image")
    axes[1][1].imshow(fftImage(imgCanny[2]), cmap=plt.get_cmap("gray"))

    figure.tight_layout()
    plt.show()

def plotAll(image):
    """ Plot all variants with image given

    image : image to plot in multiple variants
    """
    plotImageRGB(image)
    plotImageCMY(image)
    plotGrayscaleImage(image)
    plotImageCanny(image)
    plotImageFFT(image)
