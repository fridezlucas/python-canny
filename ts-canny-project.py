""" TS Canny Project

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

print("ts-canny-project\nAuthors : Fridez Lucas, Goffinet Edouard, Laissue Luca\nVersion : 1.0\n\n")

# Import All modules
import lib.file_selector as file_selector

def main():
    file_selector.chooseAnImage("img")

if(__name__ == "__main__"):
    main()
