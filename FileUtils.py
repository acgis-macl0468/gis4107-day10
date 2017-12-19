# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import os
def main():
    pass

def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass




def getFileContent(fileName):
    script_folder = os.path.dirname(os.path.abspath(__file__))
    fileName = os.path.join(script_folder,"demo.txt")
    outfile = open("C:\\acgis\\gis4107_Intro2Prog\\day10\\lab\\demo.txt","r")
    xyz = outfile.read()

    return "demo.txt"

    outfile.close()


if __name__ == '__main__':
    main()