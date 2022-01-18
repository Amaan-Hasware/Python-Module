# Python Scripting:
#                   Scripting means writing a program to automate a task
# Libraries:
# 1) OS Library ( Operating System )
# 2) Time Module

# ---------------------------------- OS Library ----------------------------------

import os
import time
import smtplib

def current_directory():
    cwd = os.getcwd()  # It gives the location of the current directory
    print(cwd)


def file_path(filename):
    path = os.path.abspath(filename)  # There are 2 paths, Absolute and Relative
    # Abs path stands for absolute path which gives the pathname right from the C Drive/ D Drive
    print(path)


current_directory()

filename = "Sample.txt"  # A sample file having the 'filename' as 'filename'
file_path(filename)


# ---------------------------------- Time Module ----------------------------------
epc = time.time()
print(epc)  # this will return time in seconds since the epoch time (1970 jan 1)
localtime = time.localtime(epc)  # it will give the local time
print(localtime)
# To extract a particular constraint such as year or month or day use the keyword 'tm'
print(localtime.tm_year)
