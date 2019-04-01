import os

from os import path


def rename(filepath, file_name):
        # make a duplicate of an existing file
    if path.exists(filepath):
        # get the path to the file in the current directory
        print(file_name)
        # rename the original file
        os.rename("temp.csv", file_name)
