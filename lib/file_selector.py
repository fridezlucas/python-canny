""" File Selector module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

import os
import glob
import sys


def getAllFiles(dir):
    """ Get all images files

    Only keep images files (*.png *.jpg *.jpeg)

    Return : list files
    """

    fileExtensions = ("*.png", "*.jpeg", "*.jpg", "*.gif")

    listFiles = []
    for files in fileExtensions:
        listFiles.extend(glob.glob(f"{dir}/{files}"))

    return listFiles


def writeAllFiles(files):
    """ Write a list of file with index
    """

    i = 0
    for f in files:
        print(f"[{i}] : {f}")
        i += 1


def chooseAnImage(dir):
    """ Allow users to choose an image from a list

    dir : directory in which user will choose image

    Return : chosen Image path
    """
    files = getAllFiles(dir)
    writeAllFiles(files)

    if(len(files) > 0):
        indexImage = (int)(input("Which img would you like to analyse : "))

        chosenImg = files[indexImage]
        print(f"Image chosen : {chosenImg}")

        return chosenImg
    else:
        print("No images found in directory '{dir}' !", file=sys.stderr)
