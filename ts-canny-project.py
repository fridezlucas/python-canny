""" TS Canny Project

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

# Import All modules
import lib.file_selector as file_selector
import os
import platform

def clearShell():
    """ Clear Shell according to current OS

    Run os.system command : cls on Windows; clear otherwise
    """
    currentOs = platform.system()
    if(currentOs == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def main():
    """Main method

    All project is run from this line
    """

    # Show contributors
    clearShell()
    print("ts-canny-project")
    print("Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca")
    print("Version : 1.0\n")

    # Run main program
    directory = f"{os.getcwd()}/img"
    file_selector.chooseAnImage(directory)


# Main Program
if(__name__ == "__main__"):
    main()
