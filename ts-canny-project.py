""" TS Canny Project

Project for TS lesson in Bsc 2

Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca
Date    : 2020.04.21
Version : 1.0
"""

# Import all modules
import lib.file_selector as file_selector
import lib.plotter as plotter
import os
import platform


def clear_shell():
    """ Clear Shell according to current OS

    Run os.system command : cls on Windows; clear otherwise
    """
    current_os = platform.system()
    if(current_os == "Windows"):
        os.system("cls")
    else:
        os.system("clear")


def main():
    """Main method

    All project is run from this line
    """

    # Show contributors
    clear_shell()
    print("ts-canny-project")
    print("Authors : Fridez Lucas, Goffinet Edouard, Laissue Luca")
    print("Version : 1.0\n")

    # Run main program
    directory = f"{os.getcwd()}/img"
    image_path = file_selector.choose_an_image(directory)

    plotter.plot_all(image_path)


# Main Program
if(__name__ == "__main__"):
    main()
