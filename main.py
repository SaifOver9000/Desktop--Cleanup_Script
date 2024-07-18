import os

#TODO: Build a Script that checks if there are files in the Directory
def file_exist(path):
    files = os.listdir(path)
    #filters out only the files.
    files = [f for f in files if os.path.isfile(path+'/'+f)]
    if len(files) != 0:
        return True
    else:
        return False
#TODO: Build a Script that Moves files from One directory to another

#TODO: Build a Script that Lists out the type of files in the directory
#TODO: Create a folder for each file type
#TODO: Move File into Associated folder, DONT touch folders.

#TODO: Find a way to run the code ccontinously in the background


