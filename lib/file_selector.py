""" File Selector module

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

# Import all modules
import os
import glob
import sys


def get_all_files(dir):
    """ Get all images files

    Only keep images files (*.png *.jpg *.jpeg)

    Return : list files
    """

    file_extensions = ("*.png", "*.jpeg", "*.jpg", "*.gif")

    list_files = []
    for files in file_extensions:
        list_files.extend(glob.glob(f"{dir}/{files}"))

    return list_files


def write_all_files(files):
    """ Write a list of file with index
    """

    i = 0
    for f in files:
        print(f"[{i}] : {f}")
        i += 1


def choose_an_image(dir):
    """ Allow users to choose an image from a list

    dir : directory in which user will choose image

    Return : chosen Image path
    """
    files = get_all_files(dir)
    write_all_files(files)

    if(len(files) > 0):
        index_image = (int)(input("Which img would you like to analyse : "))

        chosen_img = files[index_image]
        print(f"Image chosen : {chosen_img}")

        return chosen_img
    else:
        print("No images found in directory '{dir}' !", file=sys.stderr)
