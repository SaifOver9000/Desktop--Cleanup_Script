import os
from pathlib import Path

#TODO: Build a function that checks if there are files in a directory, Returns True if files are present

def fileCheck():
    directory = 'C:\\Users\\Saif\\OneDrive\\Desktop'
    files = os.listdir(directory)
    #filter to get only the files.
    files = [f for f in files if os.path.isfile(directory + '/' +f)]

    if len(files) == 0:
       return False
    else:
        return True
#TODO: Create a function that detects the types of files in the directory

def file_TypeCheck(filetype):
    p = Path('C:\\Users\\Saif\\OneDrive\\Desktop')
    
    files = [x for x in p.iterdir() if x.suffix == f".{filetype}" ] #example text file type
    
    for file in files:
        print(file)

#TODO: Buid a function that moves files from one directory to another.

#TODO: create a folder based on the file types detected

#TODO: Dont touch the folders in the current directory.

#TODO: Make the Program run in the background

#TODO: Upload this to the repo
file_TypeCheck("docx")