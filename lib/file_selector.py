""" File Selector module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

import os


def getAllFiles(dir):
    """ Get all images files

    Only keep images files (*.png *.jpg *.jpeg)
    """

    listFiles = []
    for root, directories, files in os.walk(dir):
        for file in files:
            listFiles.append(os.path.join(root, file))

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
    """
    files = getAllFiles(dir)
    writeAllFiles(files)

    indexImage = (int)(input("Which img would you like to analyse : "))

    print(f"Image chosen : {files[indexImage]}")
